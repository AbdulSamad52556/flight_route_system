from django.shortcuts import render, redirect
from .models import Route
from .forms import RouteForm, SearchNthNodeForm, ShortestPathForm
from django.contrib import messages
import heapq

def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            # Add success message
            messages.success(request, 'Route added successfully!')
            return redirect('add_route')
    else:
        form = RouteForm()
    
    # Get recent routes for display
    recent_routes = Route.objects.all().order_by('-id')
    
    return render(request, 'add_route.html', {
        'form': form,
        'recent_routes': recent_routes
    })

def find_nth_node(request):
    result = None
    if request.method == 'POST':
        form = SearchNthNodeForm(request.POST)
        if form.is_valid():
            start_airport = form.cleaned_data['start_airport']
            direction = form.cleaned_data['direction']
            steps = form.cleaned_data['steps']
            # Traverse the route
            current_airport = start_airport
            # for i in range(steps):
            try:
                next_route = Route.objects.get(
                    from_airport=current_airport, 
                    direction=direction,
                    position=steps
                )
                current_airport = next_route.to_airport
            except Route.DoesNotExist:
                current_airport = None
                    # break
            
            result = current_airport
    else:
        form = SearchNthNodeForm()
    
    return render(request, 'find_nth_node.html', {
        'form': form, 
        'result': result
    })

def longest_route(request):
    longest = Route.objects.order_by('-duration').first()
    all_routes = Route.objects.all().order_by('-duration')
    
    return render(request, 'longest.html', {
        'longest_route': longest,
        'all_routes': all_routes
    })

def shortest_path(request):
    result = None
    if request.method == 'POST':
        form = ShortestPathForm(request.POST)
        if form.is_valid():
            from_airport = form.cleaned_data['from_airport']
            to_airport = form.cleaned_data['to_airport']
            
            # Simple BFS to find shortest path
            result = find_shortest_path(from_airport, to_airport)
    else:
        form = ShortestPathForm()
    
    return render(request, 'shortest.html', {
        'form': form, 
        'result': result
    })

def find_shortest_path(start, end):
    """Dijkstra's algorithm to find shortest path based on duration"""
    
    if start == end:
        return {'path': [start], 'total_duration': 0}
    
    # Priority queue: (total_duration, current_airport, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))
    
    visited = set()
    # Track shortest known duration to each airport
    shortest_duration = {start: 0}

    print(priority_queue)
    
    while priority_queue:
        current_duration, current_airport, path = heapq.heappop(priority_queue)
        
        if current_airport == end:
            return {
                'path': path,
                'total_duration': current_duration
            }
        
        if current_airport in visited:
            continue
            
        visited.add(current_airport)
        
        # Get all routes from current airport
        outgoing_routes = Route.objects.filter(from_airport=current_airport)
        
        for route in outgoing_routes:
            if route.to_airport not in visited:
                new_duration = current_duration + route.duration
                new_path = path + [route.to_airport]
                
                # Only consider this path if it's shorter than what we've seen
                if route.to_airport not in shortest_duration or new_duration < shortest_duration[route.to_airport]:
                    shortest_duration[route.to_airport] = new_duration
                    heapq.heappush(priority_queue, (new_duration, route.to_airport, new_path))
    
    return None  # No path found
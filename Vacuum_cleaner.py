import heapq
class Room:
    def __init__(self, path):
        self.path = path

    def display(self):
        for row in self.path:
            print(row)
        print()
def dijkstra_clean(room, start):
    grid = room.path
    rows = len(grid)
    cols = len(grid[0])   
    pq = [(0, start[0], start[1], [start])]
    visited = set()
    while pq:
        distance, r, c, path_taken = heapq.heappop(pq)

        if (r, c) in visited:
            continue

        visited.add((r, c))        
        if grid[r][c] == 1:
            grid[r][c] = 0

            print(f"Cleaned node ({r}, {c})")
            print("Path taken:", path_taken)
            room.display()        
        directions = [
            (-1, 0),  
            (1, 0),  
            (0, -1),  
            (0, 1)    
        ]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited:
                    heapq.heappush(
                        pq,
                        (
                            distance + 1,
                            nr,
                            nc,
                            path_taken + [(nr, nc)]
                        )
                    )
def clean_all_rooms(rooms):
    for i, room in enumerate(rooms):
        print(f"\n ROOM {i + 1} ")

        start = (0, 0)

        dijkstra_clean(room, start)

        print("Room cleaned:")
        room.display()

        print("Moving to remaining room...")
      

room1 = Room([
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
])
room2 = Room([
  [0,0,0],
  [0,0,1],
  [0,0,0]
])

rooms = [room1,room2]

clean_all_rooms(rooms)
print(f"the bot is in the last room {len(rooms)}")

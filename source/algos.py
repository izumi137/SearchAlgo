import pygame
import random
import math
#import heapq
from queue import PriorityQueue
from const import*
from maze import SearchSpace


def Euclidean_distance (g: SearchSpace, id: int):
    d_x = g.goal.rect.x - g.grid_cells[id].rect.x
    d_y = g.goal.rect.y - g.grid_cells[id].rect.y
    return math.sqrt(d_x**2 + d_y**2)

def Manhattan_distance (g: SearchSpace, id: int):
    d_x = g.goal.rect.x - g.grid_cells[id].rect.x
    d_y = g.goal.rect.y - g.grid_cells[id].rect.y
    return abs(d_x) + (d_y)

def DFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement DFS algorithm')

    n = g.start
    open_set = [n.id]
    closed_set = []
    father = [-1]*g.get_length()

    
    while (g.is_goal(n)==0):
        x = open_set.pop()
        closed_set.append(x)
        n = g.grid_cells[x]
        if (n.id != g.start.id) and (n.id != g.goal.id):
            n.set_color(BLUE,sc)
            n.draw(sc)
        step = g.get_neighbors(n)
        for i in range(len(step)):
            n_next = random.randint(0, len(step)-1)
            if step[n_next].id not in closed_set and step[n_next].id not in open_set:
                father[step[n_next].id] = x
                if (step[n_next].id != g.start.id) and (step[n_next].id!=g.goal.id):
                    step[n_next].set_color(RED,sc)
                    step[n_next].draw(sc)
                open_set.append(step[n_next].id)
    if (g.is_goal(n)):    
        while (n.id != 0):
            x = g.grid_cells[father[n.id]]
            pygame.draw.line(sc, WHITE, n.rect.center, x.rect.center, width = 2)
            pygame.display.update()
            n = g.grid_cells[father[n.id]]
    else:
        print("Khong tim thay dich")
    #raise NotImplementedError('not implemented')

def BFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement BFS algorithm')

    n = g.start
    open_set = [n.id]
    closed_set = []
    father = [-1]*g.get_length()

    while (g.is_goal(n)==0):
        x = open_set.pop(0)
        closed_set.append(x)
        n = g.grid_cells[x]
        if (n.id != g.start.id) and (n.id != g.goal.id):
            n.set_color(BLUE,sc)
            n.draw(sc)
        n_next = g.get_neighbors(n)
        for i in n_next:
            if i.id not in open_set and i.id not in closed_set:
                father[i.id] = n.id
                if i.id != g.start.id and i.id != g.goal.id:
                    i.set_color(RED, sc)
                    i.draw(sc)
                open_set.append(i.id)

    if (g.is_goal(n)):    
        while (n.id != 0):
            x = g.grid_cells[father[n.id]]
            pygame.draw.line(sc, WHITE, n.rect.center, x.rect.center, width = 2)
            pygame.display.update()
            n = g.grid_cells[father[n.id]]
    else:
        print("Khong tim thay dich")

    #raise NotImplementedError('not implemented')

def UCS(g: SearchSpace, sc: pygame.Surface):
    print('Implement UCS algorithm')

    # +1 respect if you can implement UCS with a priority queue
    # n = g.start
    # open_set = [(0, n.id)]
    # heapq.heapify(open_set)
    # closed_set = []
    # father = [-1]*g.get_length()
    # cost = [100_000]*g.get_length()
    # cost[g.start.id] = 0

    # while(g.is_goal(n)==0):
    #     if (len(open_set)==0):
    #         break
    #     x = open_set.pop(0)
    #     n = g.grid_cells[x[1]]
    #     closed_set.append(x[1])
    #     #cost[n.id] += 1
    #     if x[1] != g.start.id and x[1] != g.goal.id:
    #         n.set_color(BLUE, sc)
    #         n.draw(sc)
        
    #     neighbors = g.get_neighbors(n)

    #     for i in neighbors:
    #         n_cost = cost[n.id] +1 
    #         if i.id not in closed_set:
    #             if (len(open_set) == 0):
    #                 heapq.heappush(open_set,(n_cost, i.id))
    #                 cost[i.id] = n_cost
    #                 father[i.id] = n.id
    #                 if i.id != g.start.id and i.id != g.goal.id:
    #                     i.set_color(RED, sc)
    #                     i.draw(sc)
    #             else:
    #                 check = 0
    #                 for o in range(len(open_set)):
    #                     if open_set[o][1] == i.id :
    #                         check = 1
    #                         if open_set[o][0] > n_cost:
    #                             open_set[o] = (n_cost,open_set[o][0])
    #                             cost[i.id] = n_cost
    #                             father[i.id] = n.id
    #                             #heapq.heapify(open_set)
    #                         break
    #                 if check == 0:
    #                     heapq.heappush(open_set,(n_cost, i.id))
    #                     cost[i.id] = n_cost
    #                     father[i.id] = n.id
    #                     if i.id != g.start.id and i.id != g.goal.id:
    #                         i.set_color(RED, sc)
    #                         i.draw(sc)

    #print(cost[g.goal.id])
    n = g.start
    open_set = [(0, n.id)]
    closed_set = []
    father = [-1]*g.get_length()
    cost = [100_000]*g.get_length()
    cost[g.start.id] = 0

    
    while(g.goal.id not in closed_set):
        if (len(open_set) == 0):
            break
        PQ = PriorityQueue()
        for i in range(len(open_set)):
            PQ.put(open_set[i])
        x = PQ.get()
        n = g.grid_cells[x[1]]
        open_set.remove(x)

        if n.id in closed_set:
            continue
        closed_set.append(x[1])
        
        
        #cost[n.id] += 1
        if x[1] != g.start.id and x[1] != g.goal.id:
            n.set_color(BLUE, sc)
            n.draw(sc)
        
        neighbors = g.get_neighbors(n)

        for i in neighbors:
            weight = random.randint(0,50)
            n_cost = cost[n.id] + weight
            if i.id not in closed_set:
                check = 0
                for j in range (len(open_set)):
                    if open_set[j][1] == i.id:
                        check = 1
                        if open_set[j][0] > n_cost:
                            open_set[j] = (n_cost,i.id)
                            cost[i.id] = n_cost
                            father[i.id] = n.id
                        break
                if check == 0:
                    open_set.append((n_cost,i.id))
                    cost[i.id] = n_cost
                    father[i.id] = n.id
                if i.id != g.start.id and i.id != g.goal.id:
                    i.set_color(RED, sc)
                    i.draw(sc)


    if (g.is_goal(n)):   
        while (n.id != 0):
            x = g.grid_cells[father[n.id]]
            pygame.draw.line(sc, WHITE, n.rect.center, x.rect.center, width = 2)
            pygame.display.update()
            n = g.grid_cells[father[n.id]]
    else:
        print("Khong tim thay dich")
    #raise NotImplementedError('not implemented')

def Greedy(g: SearchSpace, sc: pygame.Surface):
    print('Implement Greedy algorithm')

    n = g.start
    open_set = [(Manhattan_distance(g,n.id), n.id)]
    closed_set = []
    father = [-1]*g.get_length()

    # Heuristic function is Euclidean distance between current node and goal
    while(g.goal.id not in closed_set):
        if (len(open_set) == 0):
            break
        PQ = PriorityQueue()
        for i in range(len(open_set)):
            PQ.put(open_set[i])
        x = PQ.get()
        n = g.grid_cells[x[1]]
        open_set.remove(x)

        if n.id in closed_set:
            continue
        closed_set.append(x[1])
        if x[1] != g.start.id and x[1] != g.goal.id:
            n.set_color(BLUE, sc)
            n.draw(sc)
        
        neighbors = g.get_neighbors(n)
        for i in neighbors:
            Heuristic = Manhattan_distance(g, i.id)
            if i.id not in closed_set:
                check = 0
                for j in range (len(open_set)):
                    if open_set[j][1] == i.id:
                        check = 1
                        if open_set[j][0] > Heuristic:
                            open_set[j] = (Heuristic,i.id)
                            father[i.id] = n.id
                        break
                if check == 0:
                    open_set.append((Heuristic,i.id))
                    father[i.id] = n.id
                if i.id != g.start.id and i.id != g.goal.id:
                    i.set_color(RED, sc)
                    i.draw(sc)

    if (g.is_goal(n)):    
        while (n.id != 0):
            x = g.grid_cells[father[n.id]]
            pygame.draw.line(sc, WHITE, n.rect.center, x.rect.center, width = 2)
            pygame.display.update()
            n = g.grid_cells[father[n.id]]
    else:
        print("Khong tim thay dich")

    #raise NotImplementedError('not implemented')
def AStar(g: SearchSpace, sc: pygame.Surface):
    print('Implement AStar algorithm')

    # +1 respect if you can implement AStar with a priority queue
    n = g.start
    open_set = [(Manhattan_distance(g,n.id), n.id)]
    closed_set = []
    father = [-1]*g.get_length()
    cost = [100_000]*g.get_length()
    cost[g.start.id] = 0

    # Heuristic function is Euclidean distance between current node and goal
    while(g.goal.id not in closed_set):
        if (len(open_set) == 0):
            break
        PQ = PriorityQueue()
        for i in range(len(open_set)):
            PQ.put(open_set[i])
        x = PQ.get()
        n = g.grid_cells[x[1]]
        open_set.remove(x)

        # if n.id in closed_set:
        #     continue
        closed_set.append(x[1])
        if x[1] != g.start.id and x[1] != g.goal.id:
            n.set_color(BLUE, sc)
            n.draw(sc)
        
        neighbors = g.get_neighbors(n)
        for i in neighbors:
            Heuristic = Manhattan_distance(g, i.id)
            weight = random.randint(0,50)
            n_cost = cost[n.id] + weight
            f = Heuristic + n_cost
            if i.id not in closed_set:
                check = 0
                for j in range (len(open_set)):
                    if open_set[j][1] == i.id:
                        check = 1
                        if open_set[j][0] + Manhattan_distance(g,i.id) > f:
                            open_set[j] = (f,i.id)
                            cost[i.id] = n_cost
                            father[i.id] = n.id
                        break
                if check == 0:
                    open_set.append((f,i.id))
                    cost[i.id] = n_cost
                    father[i.id] = n.id
                if i.id != g.start.id and i.id != g.goal.id:
                    i.set_color(RED, sc)
                    i.draw(sc)

    if (g.is_goal(n)):   
        while (n.id != 0):
            x = g.grid_cells[father[n.id]]
            pygame.draw.line(sc, WHITE, n.rect.center, x.rect.center, width = 2)
            pygame.display.update()
            n = g.grid_cells[father[n.id]]
    else:
        print("Khong tim thay dich")
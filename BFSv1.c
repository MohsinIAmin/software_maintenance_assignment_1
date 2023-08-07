#include <stdio.h>

#define WHITE 0
#define GREAY 1
#define BLACK 2
// Color

#define MAX_NODE 100

int graph[MAX_NODE][MAX_NODE];
int color[MAX_NODE], previous[MAX_NODE], dis[MAX_NODE];

void a_old_function()
{
    for (int j = 0; j < 1000; j++)
    {
        printf("%d", j);
    }
}

void another_old_function() {}

void initialize_graph(int number_of_nodes)
{
    for (int i = 0; i < number_of_nodes; i++)
    {
        for (int j = 0; j < number_of_nodes; j++)
        {
            graph[i][j] = 0;
        }
    }
}

void init_graph(int number_of_nodes, int number_of_edge)
{
    while (number_of_edge--)
    {
        int sourse, destination;
        scanf("%d%d", &sourse, &destination);
        graph[sourse][destination] = 1; // A directed graph
    }
}

void print_graph(int number_of_nodes)
{
    for (int i = 0; i < number_of_nodes; i++)
    {
        for (int j = 0; j < number_of_nodes; j++)
        {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
}

void bfs(int sourse, int number_of_nodes)
{
    for (int i = 0; i < number_of_nodes; i++)
    {
        color[i] = WHITE;
        dis[i] = -1;
        previous[i] = -1;
    }
    color[sourse] = GREAY;
    dis[sourse] = 0;
    previous[sourse] = 0;
    int front = 0, rear = 0;
    int queue[number_of_nodes];
    queue[rear++] = sourse;
    while (front != rear)
    {
        int visiting = queue[front++];
        for (int to_visit = 0; to_visit < number_of_nodes; to_visit++)
        {
            if (graph[visiting][to_visit] == 1)
            {
                if (color[to_visit] == WHITE)
                {
                    color[to_visit] = GREAY;
                    dis[to_visit] = dis[visiting] + 1;
                    previous[to_visit] = visiting;
                    queue[rear++] = to_visit;
                }
            }
        }
        color[visiting] = BLACK;
    }
}

void print_path(int sourse, int destination)
{
    if (sourse == destination)
    {
        printf("%d->", sourse);
    }
    else if (dis[destination] == -1)
    {
        printf("NO PATH");
    }
    else
    {
        print_path(sourse, previous[destination]);
        printf("%d->", destination);
    }
}

int main(int argc, char *argv[])
{
    int number_of_nodes = 0, number_of_edge = 0, sourse = 0, destination = 0;
    scanf("%d", &number_of_nodes);
    initialize_graph(number_of_nodes);
    scanf("%d", &number_of_edge);
    init_graph(number_of_nodes, number_of_edge);
    print_graph(number_of_nodes);
    scanf("%d", &sourse);
    scanf("%d", &destination);
    bfs(sourse, number_of_edge);
    for (int i = 0; i < number_of_nodes; i++)
    {
        print_path(sourse, i);
        printf("\n");
    }
    print_path(sourse, destination);
    return 0;
}

# Job Scheduling (Graph)
class Graph:
    def __init__(self):
        self.jobs = []
        self.graph = {}
        self.dependencies = []

    def add_job(self, job):
        if job not in self.graph:
            self.jobs.append(job)
            self.graph[job] = []

    def add_dependency(self, first_job, second_job):
        if (first_job, second_job) not in self.dependencies:
            self.dependencies.append((first_job, second_job))
            self.graph[first_job].append(second_job)

    def display_graph(self):
        print("\n  Job Dependency Graph:")

        # Print dependencies in the entered sequence
        for first_job, second_job in self.dependencies:
            print(first_job, "->", second_job)


class JobScheduler:
    def __init__(self, graph):
        self.graph = graph

    def schedule_jobs(self):
        indegree = {job: 0 for job in self.graph.jobs}

        for job in self.graph.jobs:
            for next_job in self.graph.graph[job]:
                indegree[next_job] += 1

        queue = []

        for job in self.graph.jobs:
            if indegree[job] == 0:
                queue.append(job)

        schedule = []

        while queue:
            current_job = queue.pop(0)
            schedule.append(current_job)

            for next_job in self.graph.graph[current_job]:
                indegree[next_job] -= 1

                if indegree[next_job] == 0:
                    queue.append(next_job)

        if len(schedule) == len(self.graph.jobs):
            print("\n  Correct Job Scheduling Order:")
            print(" -> ".join(schedule))
        else:
            print("\nCircular dependency detected!")
            print("Jobs cannot be scheduled.")


def main():
    graph = Graph()

    print("\n====== JOB SCHEDULING SYSTEM ======")
    project_title = input("\nproject title: ")
    number_of_jobs = int(input("\nEnter number of jobs:"))

    for i in range(number_of_jobs):
        job = input("Enter job name: ").strip()
        graph.add_job(job)

    number_of_dependencies = int(
        input("\nEnter number of dependencies: ")
    )

    print("\nEnter dependencies (first job before second job):")

    for i in range(number_of_dependencies):
        while True:
            first_job = input("Enter first job: ").strip()
            second_job = input("Enter second job: ").strip()

            if (first_job in graph.graph and
                    second_job in graph.graph):
                graph.add_dependency(first_job, second_job)
                break
            else:
                print("Invalid job name. Please enter again.")

    graph.display_graph()

    scheduler = JobScheduler(graph)
    scheduler.schedule_jobs()


main()

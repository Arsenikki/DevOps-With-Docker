***Kubernetes - All-in-one solution to container management?***

Containers have become popular as they provide an easy way to package and deploy applications with the required dependencies as well as providing isolalated environment for your services. Kubernetes is an open-source container management system, which helps managing these containers. It was originally created by Google and it has gained huge popularity, but not without a reason.  

In production, a system may have dozens, possibly even thousands of containers in use simultaneously. These containers need to be deployed, managed, connected and updated. This is the main reason to use container management system, such as Kubernetes. 

In my opinion, scalability and load balancing are the most important features that Kubernetes provides. This means that depending on the demand, the workload can be split in to multiple processes and each micro-service can be scaled individually depending on the load. Kubernetes also does automated health checks on the containers and will handle starting, closing and restarting by itself. All this with endless configuration possibilities. 

Docker also has a similar service called Docker Swarm, which can manage clusters of Docker containers by combining multiple Docker hosts into single host. Docker Swarm provides simple and quick way to deploy multiple Docker containers, but it lacks in the amount of features when compared to all in one solution of Kubernetes. 
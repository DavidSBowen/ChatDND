# ChatDND

Just a couple of gamers

# Up and Running

## Requirements
Docker Compose (v2.18.0+)
Docker (23.0.5+)

## Quickstart
There are 3 commands in the Makefile. Use them from the directory the Makefile is in, which is the repository's root directory.
- `make up`
    - starts the FE, BE, and DB in Docker containers via docker-compose
- `make down`
    - shuts down the FE, BE, and DB containers
- `make reset` - **use this for ease of use**
    - runs `make down` then `make up`, effectively restarting the environment.

**Note that resetting currently kills the database state and starts a new one**

# Links

## GitHub
[Full Project Ticket Backlog](https://github.com/users/DavidSBowen/projects/1/views/1)

[Ticket Kanban board](https://github.com/users/DavidSBowen/projects/1/views/2)

## Brainstorm
[Google Docs Brainstorming](https://docs.google.com/document/d/1mlByvbyyMYlVMzv-P9Vy5uGSBC63b7gL9r9FGdApFWE/edit#)

[Whimsical Diagrams](https://whimsical.com/everyone-in-workspace-3Q9HkRhViFmfyoUjoEmW5U)

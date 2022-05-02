# Development guide

## Quick start

1. Fork the repository to your github account.

1. Clone your forked repository.

   ```sh
   git clone -o upstream git@github.com:GITHUB_USER/YOUR_CLONED_REPO.git
   cd YOUR_CLONED REPO
   ```

1. Add dependencies by `make requirements-dev`.

1. Create a new branch: `git checkout -b my-awesome-feature`.

1. Write your code at `api/` directory.

1. Update/add required documentation at `docs/`.

1. Write your tests at `tests/`.

1. Execute tests by `make test`.

1. You can check the swagger documentation by `make run`
   and accessing to `http://localhost:5000/apidocs`. And check
   the API at `http://localhost:5000/api/hello/world`.

1. Check linters by `make lint`.

1. Push your change
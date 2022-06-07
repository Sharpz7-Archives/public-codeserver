import os

BANNED = ["build.py", "builds"]
EXECUTOR_COUNT = 30


def split_builds(all_builds, no_of_executors):
    """
    Splits Builds into n equal parts
    """

    return [all_builds[i::no_of_executors] for i in range(no_of_executors)]


class Build:
    """
    Class for Build
    """

    def __init__(self, folder):
        self.name = "codeserver"
        self.folder = folder
        self.version = self.check_version()

    def check_version(self):
        """
        Reads for .version file
        """

        if os.path.isfile(f"./{self.folder}/.version"):
            with open(f"./{self.folder}/.version", 'r') as file:
                return file.read()

        else:
            return "latest"

    def __repr__(self):
        return f"{self.name}, {self.version}"


def main():
    """
    Main function
    """

    locs = os.listdir(".")
    builds = []
    for loc in locs:
        if loc not in BANNED:
            builds.append(Build(loc))
    split = split_builds(builds, EXECUTOR_COUNT)

    for num, executor in enumerate(split):
        job_code = ""

        for build in executor:
            shell = (
                "set -e\n"
                f"docker login -u $DOCKER_USER -p $DOCKER_PASS"
                f"docker pull sharp6292/{build.name}:{build.version} || true\n"
                f"docker build --cache-from sharp6292/{build.name}:{build.version}"
                f" -f dockerfiles/{build.folder}/Dockerfile "
                f"-t sharp6292/{build.name}:{build.version} .\n"
                f"docker login -u $DOCKER_USER -p $DOCKER_PASS"
                f"docker push sharp6292/{build.name}:{build.version}\n"
            )
            job_code += shell

        with open(f'./builds/build-{num}.sh', 'w') as file:
            file.write(job_code)
            print(shell)


if __name__ == "__main__":
    main()

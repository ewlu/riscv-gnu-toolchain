import argparse
from github import Auth, Github
from download_artifacts import download_artifact


def parse_arguments():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Download single log artifact")
    parser.add_argument(
        "-name",
        required=True,
        type=str,
        help="Name of the artifact",
    )
    parser.add_argument(
        "-token",
        required=True,
        type=str,
        help="Github access token",
    )
    parser.add_argument(
        "-outdir",
        required=True,
        type=str,
        help="output dir to put downloaded file"
    )
    parser.add_argument(
        "-repo",
        default="patrick-rivos/riscv-gnu-toolchain",
        type=str,
        help="which repo to pull from"
    )
    parser.add_argument(
        "-zip",
        default=None,
        type=str,
        help="which repo to pull from"
    )
    return parser.parse_args()


def download_artifact_with_name(artifact_name: str, token: str, outdir: str, repo_name: str, zip_name: str):
    """
    Download the artifact with a given name into ./logs.
    """
    auth = Auth.Token(token)
    g = Github(auth=auth)

    repo = g.get_repo(repo_name)

    artifacts = repo.get_artifacts(artifact_name).get_page(0)
    if len(artifacts) != 0:
        download_artifact(artifact_name, str(artifacts[0].id), token, outdir, repo=repo_name, artifact_zip_name=zip_name)
    else:
        raise ValueError(f"Failed to find artifact for {artifact_name}")


def main():
    args = parse_arguments()
    download_artifact_with_name(args.name, args.token, args.outdir, args.repo, args.zip)


if __name__ == "__main__":
    main()

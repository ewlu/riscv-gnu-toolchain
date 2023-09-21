import requests
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Send api response")
    parser.add_argument(
        "-pid",
        "--patch-id",
        metavar="<string>",
        required=True,
        type=str,
        help="Patch id",
    )
    parser.add_argument(
        "-desc",
        "--description",
        metavar="<string>",
        required=True,
        type=str,
        help="Check type (linter, build, etc)",
    )
    parser.add_argument(
        "-state",
        "--state",
        metavar="<string>",
        default="pending"
        type=str,
        help="check state",
    )
    parser.add_argument(
        "-context",
        "--context",
        required=True,
        metavar="<string>",
        type=str,
        help="What test we reporting for",
    )
    parser.add_argument(
        "-rid",
        "--run-id",
        metavar="<string>",
        type=str,
        help="run id",
    )
    parser.add_argument(
        "-iid",
        "--issue-id",
        metavar="<string>",
        type=str,
        help="issue number",
    )
    return parser.parse_args()

def send(patch_id: str, desc: str, issue: str, rid: str, state: str, context: str):
    target_url = None
    if issue == "":
        target_url = f"https://github.com/ewlu/riscv-gnu-toolchain/actions/runs/{rid}"
    else:
        target_url = f"https://github.com/ewlu/riscv-gnu-toolchain/issues/{issue}"
    url = f"https://patchwork.sourceware.org/api/1.3/patches/{patch_id}/checks/"
    params = {
        "state": state,
        "target_url": target_url,
        "context": f"toolchain-ci-rivos/{context}",
        "description": desc
    }

    # x = requests.post(url, json=params)
    # print(x.text)
    print(f"target: {target_url}")
    print(f"post url: {url}")
    print(f"params: {params}")

def main():
    args = parse_arguments()
    send(args.patch_id, args.description, args.issue_id, args.run_id, args.state, args.context)

if __name__ == "__main__":
    main()

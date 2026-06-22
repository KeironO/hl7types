import glob

import nox


@nox.session(python=["3.10", "3.11", "3.12", "3.13", "3.14"])
def tests(session):
    session.run("uv", "sync", "--group", "dev", "--active", external=True)
    session.run("uv", "run", "--active", "pytest")


@nox.session(python=["3.10", "3.11", "3.12", "3.13", "3.14"])
def examples(session):
    session.run("uv", "sync", "--group", "dev", "--active", external=True)
    for script in sorted(glob.glob("examples/*.py")):
        session.run("uv", "run", "--active", "python", script, external=True)

import glob

import nox


@nox.session(python=["3.10", "3.11", "3.12", "3.13"])
def tests(session):
    session.run("uv", "sync", "--group", "dev", external=True)
    session.run("uv", "run", "pytest")


@nox.session(python=["3.10", "3.11", "3.12", "3.13"])
def examples(session):
    session.run("uv", "sync", "--group", "dev", external=True)
    for script in sorted(glob.glob("examples/*.py")):
        session.run("uv", "run", "python", script, external=True)

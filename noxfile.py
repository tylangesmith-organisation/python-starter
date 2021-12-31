import nox


@nox.session(python=["3.9"], reuse_venv=True)
def test(session):
    session.run("poetry", "install")
    session.run("pytest")


@nox.session(python=False, reuse_venv=True)
def lint(session):
    session.run("poetry", "install")
    session.run("flake8", "python_starter", "tests", "noxfile.py")


@nox.session(python=False, reuse_venv=True)
def black(session):
    session.run("poetry", "install")
    session.run("black", "python_starter", "tests", "noxfile.py")

import sys

from invoke import task

from .util import PROJECT_DIR, print_and_run

sys.path.append(str(PROJECT_DIR))

from slackbotr.constants.paths import PACKAGE_DIR, PROJECT_DIR, SCRIPTS_DIR


@task
def shellcheck(ctx):
    # FIXME: It's unclear why, but the return code seems to be getting swallowed.
    print_and_run(
        f'cd {PROJECT_DIR} &&'
        f' for file in $(find {SCRIPTS_DIR} -type f -name "*.sh"); do'
        '    shellcheck $file;'
        '  done'
        f' && shellcheck {PROJECT_DIR}/deploy/deploy',
        pty=True,
    )


@task()
def formatcheck(ctx):
    """Check that the code conforms to formatting standards."""
    print_and_run(f"isort --check-only {PROJECT_DIR}")
    print_and_run(f"black --check {PROJECT_DIR}")
    print("🎉🙈 Format check passed.")


@task(aliases=('flake8',))
def lint(ctx):
    """Run static analysis with flake8."""
    print_and_run(
        f'cd {PROJECT_DIR} &&'
        f" flake8 --config {PROJECT_DIR / '.flake8'} {PACKAGE_DIR} {SCRIPTS_DIR}",
        pty=True,
    )
    # print_and_run(
    #     f'cd {PROJECT_DIR} &&'
    #     f' vulture --min-confidence 80 {PACKAGE_DIR} {SCRIPTS_DIR}',
    #     pty=True,
    # )
    print("🎉👕 Linting passed.")


@task(aliases=('mypy',))
def typecheck(ctx):
    """Check for type correctness using mypy."""
    print_and_run(f"mypy --config-file={PROJECT_DIR / '.mypy.ini'} {PACKAGE_DIR}/")
    print('🎉🦆 Type checking passed.')


@task(pre=[shellcheck, formatcheck, lint, typecheck])
def static(ctx):
    """Run all static analysis tasks."""
    pass


@task(aliases=('unit',))
def unittest(ctx):
    """Run unit tests."""
    print_and_run(
        f'PYTHONPATH={PROJECT_DIR} pytest --verbose {PACKAGE_DIR}/test/',
        pty=True,
    )
    print('🎉🛠️  Unit tests passed.')


@task(aliases=('integration',))
def integrationtest(ctx):
    """Run integration tests."""
    print_and_run(
        f'PYTHONPATH={PROJECT_DIR} pytest --verbose {PACKAGE_DIR}/test_integration',
        pty=True,
    )

    print('🎉🧩 Integration tests passed.')


@task(aliases=('regression',))
def regressiontest(ctx):
    """Run regression tests."""
    print_and_run(
        f'PYTHONPATH={PROJECT_DIR} pytest --verbose {PACKAGE_DIR}/test_regression',
        pty=True,
    )

    print('🎉⏰ Regression tests passed.')


@task(
    pre=[
        shellcheck,
        lint,
        formatcheck,
        typecheck,
        unittest,
        integrationtest,
        regressiontest,
    ],
    default=True,
)
def all(ctx):
    """Run all of the tests."""
    print("🎉❤️  All tests passed!")


@task(
    pre=[
        shellcheck,
        lint,
        formatcheck,
        typecheck,
        unittest,
        integrationtest,
    ],
)
def ci(ctx):
    """Run the tests that would be run in CI."""
    print("🎉❤️  CI tests passed!")

ARG SERVICE_NAME=notifier

FROM tutor-stack-base:latest

ENV SERVICE_NAME=${SERVICE_NAME}
ENV PORT=8000

CMD ["python", "-m", "uvicorn", "tutor_stack_notifier.main:app", "--host", "0.0.0.0", "--port", "8000"] 
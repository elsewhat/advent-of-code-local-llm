# Import via: ollama create qwk-fix-stop:latest -f qwq-fix-stop-modelfile.md
FROM qwq:latest
# Adding additional stop as otherwise the qwq model goes into an infinite loop
PARAMETER stop <|endoftext|>
# If you want to expand context window PARAMETER num_ctx 32768
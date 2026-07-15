There is an Apache-style access log at /app/access.log. Read it and produce a small JSON summary of the traffic.

Write your summary to /app/report.json as a single JSON object with exactly these three keys:

- `total_requests` (integer): the total number of request lines in the log.
- `unique_ips` (integer): the number of distinct client IP addresses. The client IP is the first whitespace-separated field of each line.
- `top_path` (string): the request path that appears most often across all requests. The request path is the path in the quoted request line, e.g. `/index.html` in `"GET /index.html HTTP/1.1"`.

Success criteria:

1. /app/report.json exists and contains a single valid JSON object.
2. `total_requests` equals the total number of request lines in /app/access.log.
3. `unique_ips` equals the number of distinct client IP addresses in the log.
4. `top_path` is the request path requested most frequently in the log.

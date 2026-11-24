# Playwright

Research checked: 2026-11-23. Verify installed versions before production.

Test the generated project in its authorized local browser environment. Install the matching browser when needed. Assert asset readiness, font loading and absence of page errors; capture frame evidence at fixed viewport dimensions. Test repeated and out-of-order frame sampling through the project's render API. Do not use screenshots alone as a complete video render. Respect the host's browser-tool policies; a managed browser session may require its provided browser API.

Starting command (run in the appropriate project/environment):

```sh
npm install --save-dev --save-exact @playwright/test
```

Official sources: [Playwright](https://playwright.dev/docs/intro) · [Details](https://playwright.dev/docs/test-snapshots)


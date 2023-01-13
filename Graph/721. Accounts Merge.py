class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # DFS
        # 1. Iterate through accounts, creating graph of emails
        # 2. DFS through emails
        # 3. Mark visited
        # 4. Add emails to res

        # Build graph
        visited = defaultdict(bool)
        graph = defaultdict(list)
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                graph[email].append(i)

        # DFS graph
        def _dfs(account, emails):
            if visited[account]:
                return None
            visited[account] = True
            # Add emails
            emails.update(accounts[account][1:])
            # DFS
            for email in accounts[account][1:]:
                for account in graph[email]:
                    _dfs(account, emails)

            return sorted(list(emails))

        res = []
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, emails = account[0], set()
            res.append([name] + _dfs(i, emails))
        return res

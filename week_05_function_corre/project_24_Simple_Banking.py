# Project 24 — Simple Banking (multiple accounts)
# EN: Use a dict accounts = {"Asha": 5000, "Rahul": 3000}. Write deposit(accounts, name, amount) and withdraw(accounts, name, amount) that update and return the dict (check the account exists and enough balance). Run a menu to operate on any account and always show the updated balances.
# हिंदी: एक dict accounts = {"Asha": 5000, "Rahul": 3000} इस्तेमाल करो। deposit(accounts, name, amount) और withdraw(accounts, name, amount) बनाओ जो dict को update करके return करें (account मौजूद है और balance काफ़ी है — check करो)। किसी भी account पर काम करने के लिए menu चलाओ और हमेशा updated balances दिखाओ।
# Concepts: dict as shared state, functions modifying and returning a dict, validation
# Hint: if name not in accounts: return accounts with a message; guard amount > accounts[name] in withdraw.

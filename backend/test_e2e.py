import urllib.request
import urllib.parse
import json

BASE = "http://localhost:5000/api"

def request(path, method="GET", data=None, token=None):
    url = f"{BASE}{path}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode("utf-8"))

print("=== 1. Health Check ===")
code, res = request("/health")
print("Health:", code, res)
assert code == 200

print("\n=== 2. Login as Freelancer ===")
code, res = request("/auth/login", method="POST", data={
    "email": "freelancer@freelancehub.com",
    "password": "free123"
})
print("Login:", code, res.get("user", {}).get("name"), "Role:", res.get("user", {}).get("role"))
assert code == 200
token = res["token"]
freelancer_id = res["user"]["id"]

print("\n=== 3. Search Talent / Freelancers ===")
code, res = request("/users/freelancers/search?q=React")
print("Search Freelancers count:", len(res))
for f in res:
    print(f" - {f['name']} (Rs. {f['hourly_rate']}/hr) Skills: {f['skills']}")
assert len(res) > 0

print("\n=== 4. View Freelancer Profile with Portfolio ===")
code, res = request(f"/users/{freelancer_id}")
print("Profile:", res["name"], "Portfolios count:", len(res["portfolio"]))
for p in res["portfolio"]:
    print(f"  * {p['title']} ({p['technologies']})")
assert len(res["portfolio"]) > 0

print("\n=== 5. Search Projects ===")
code, res = request("/projects?q=React")
print("Projects found:", len(res))
for p in res:
    print(f" - [{p['status']}] {p['title']} | Rs. {p['budget']} | Client: {p['client']}")
assert len(res) > 0
proj_id = res[0]["id"]

print("\n=== 6. Submit Proposal ===")
code, res = request(f"/applications/project/{proj_id}", method="POST", token=token, data={
    "proposal": "Expert full-stack developer with 5+ years experience. Can deliver in 6 days with full test suite.",
    "bid_amount": 41000,
    "estimated_days": 6
})
print("Proposal submit result:", code, res)
assert code == 201

print("\n=== 7. Post New Project as Client ===")
code, client_res = request("/auth/login", method="POST", data={
    "email": "client1@freelancehub.com",
    "password": "client123"
})
client_token = client_res["token"]

import time
test_title = f"Automated CI/CD Pipeline Audit #{int(time.time())}"
code, new_proj = request("/projects", method="POST", token=client_token, data={
    "title": test_title,
    "description": "Looking for DevOps expert to audit GitHub Actions pipeline and automate container security scans.",
    "skills": "Docker, GitHub Actions, Security",
    "budget": 60000,
    "deadline": "2026-11-15",
    "experience_level": "expert",
    "project_type": "fixed"
})
print("New Project Created:", code, new_proj.get("project", {}).get("title"))
assert code == 201

print("\n=== 8. Check Client Notifications ===")
code, notes = request("/notifications", token=client_token)
print("Client Notifications count:", len(notes))
for n in notes[:3]:
    msg = n['message'].encode('ascii', 'replace').decode('ascii')
    print(f" - [{n['title']}] {msg}")
assert len(notes) > 0

print("\n=== 9. Check Admin Stats ===")
code, stats = request("/admin/stats")
print("Admin Stats:", stats)
assert stats["total_projects"] >= 5

print("\n=== ALL E2E BACKEND TESTS PASSED WITH 100% SUCCESS! ===")

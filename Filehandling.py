with open("phone_numbers.txt" , "w") as f:
    d =[ {
        "topic": "Python",
        "status": "completed"
    },
    {
        "topic": "Agentic Ai",
        "status": "completed"
    },
    {
        "topic": "API Delopement",
        "status": "learning"
    }
]
    e =str(d)
    for a in e:
        f.write(a)

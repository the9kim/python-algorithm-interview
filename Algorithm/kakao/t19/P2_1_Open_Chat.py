def solution(record):
    nickname = {}

    for r in record:
        action, uid, *rest = r.split(" ", 2)
        if action in ('Enter', 'Change'):
            nickname[uid] = rest[0]

    results = []

    for r in record:
        action, uid, *_ = r.split(" ", 2)

        if action == 'Enter':
            results.append(f'{nickname[uid]}님이 들어왔습니다.')
        elif action == 'Leave':
            results.append(f'{nickname[uid]}님이 나갔습니다.')

    return results
def solution(bandage, health, attacks):
    answer = 0
    origin_health = health
    tmp = max(attacks)[0]
    attacks_cnt = 0
    success = 0
    for i in range(1, tmp + 1):
        if i == attacks[attacks_cnt][0]:
            health -= attacks[attacks_cnt][1]
            attacks_cnt += 1
            success = 0
        else:
            if health < origin_health:
                health += bandage[1]
                success += 1
                if success == bandage[0]:
                    print('추가체력 지급',i)
                    health += bandage[2]
                    success=0
            else:
                health = origin_health

        if health <= 0:
            answer = -1
            break

    if health <= 0 and attacks_cnt !=len(attacks):
        answer = -1
    elif health<=0:
        answer=-1
    else:
        answer = health
    return answer
import random 
import os
from art import logo;



"""카드 랜덤으로 리턴"""
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
    card = random.choice(cards);
    return card;

# 유저, 컴퓨터 카드 계산
def calculate_score(cards):
    # 블랙잭인 경우 0 으로 리턴
    if sum(cards) == 21 and len(cards) == 2:
        return 0;

    # 에이스 카드는 총 합이 21 보다 크면 1로 적용
    if 11 in cards and sum(cards) > 21:
        cards.remove(11);
        cards.append(1);
    
    return sum(cards);

# 점수 체크 후 메시지 처리
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw";
    elif computer_score ==0:
        return "Lose, opponent has BlackJack";
    elif user_score == 0:
        return "Win with a BlackJack";
    elif user_score > 21:
        return "You went over. You lose";
    elif computer_score>21:
        return "Opponet went over. You win";
    elif user_score > computer_score:
        return "You win";
    else:
        return "You lose";

def playGame():
    print(logo);

    isContinueGame = True;
    user =[];
    computer =[];

    for num in range(2):
        user.append(deal_card());
        computer.append(deal_card());
    
    while isContinueGame:
        
        user_score = calculate_score(user);
        computer_score = calculate_score(computer);
        print(f" Your cards: {user}, score: {user_score}");
        print(f" Computer first cards: {computer[0]}");
        if user_score == 0 or computer_score ==0 or user_score >21:
            isContinueGame = False;
        else:
            user_should_deal=  input("Type 'y' to get another card, type 'n' to pass: ");
            if user_should_deal.lower() == "y":
                user.append(deal_card());   
            else:
                isContinueGame = False;

    # 컴퓨터 점수가 17 아래이면 카드를 추가로 받음
    while computer_score !=0 and computer_score <17:
        computer.append(deal_card());  
        computer_score = calculate_score(computer);

    print(f" Your final cards: {user}, final score: {user_score}");
    print(f" Computer final cards: {computer} , final score: {computer_score}");
    print(compare(user_score, computer_score));

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls"); # clear 처리
    playGame();
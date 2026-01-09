import streamlit as st
import random

#じゃんけんプログラム

def jyanken (player_hand):
    hands = ["グー","チョキ","パー"]
    cpu_hand = random.choice(hands)
    if player_hand == cpu_hand:
        result = "あいこ！"
    elif (player_hand == "グー" and cpu_hand == "チョキ") or \
         (player_hand == "チョキ" and cpu_hand == "パー") or \
         (player_hand == "パー" and cpu_hand == "グー"):
        result = "勝利！"
    else:
        result = "負け！"
    return cpu_hand, result


#メインプログラム
def main():
    st.title("じゃんけんゲーム")
    st.text("手を選んでください")
    player_hand = st.selectbox("あなた",("グー","チョキ","パー"))
    if st.button("じゃんけんポン！"):
        cpu_hand, result = jyanken(player_hand)
        st.write(f"CPU:{cpu_hand}")
        if cpu_hand == "チョキ":
            st.image("janken_choki.png")
        elif cpu_hand == "グー":
            st.image("janken_gu.png")
        else:
        　　 st.image("janken_pa.png")
        st.write(f"結果:{result}")

if __name__ == "__main__":

    main()





import streamlit as st

def app():
    st.title("🚪 Logout")
    st.write("Are you sure you want to log out of your AI Virtual Lab account?")
    
    st.divider()
    
    col1, col2 = st.columns([1, 4])
    
    with col1:
        # Jab user confirms karega ke haan logout karna hai
        if st.button("Yes, Logout", type="primary", use_container_width=True):
            
            # 1. Session state ke saare data (username, login status) ko complete mita dein
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            
            # 2. Success message de kar browser ko fresh reload karein
            st.success("Logged out successfully!")
            st.rerun()
            
    with col2:
        if st.button("Cancel", use_container_width=False):
            # Agar cancel kare toh wapas dashboard ya editor par bhej dein
            st.info("Logout cancelled.")
            # Aap chahein toh yahan redirection dal sakti hain, optional hai
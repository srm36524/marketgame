import streamlit as st
import pandas as pd


def teacher_page():

    st.header("👨‍🏫 Teacher Control Panel")

    # ------------------------------------------
    # Simulation Status
    # ------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current Iteration",
            st.session_state.iteration
        )

    with col2:
        st.metric(
            "Teams",
            len(st.session_state.team_names)
        )

    with col3:
        st.metric(
            "Initial Capital",
            f"₹{st.session_state.initial_capital:,.0f}"
        )

    st.divider()

    # ------------------------------------------
    # Allocation Controls
    # ------------------------------------------

    st.subheader("Allocation Controls")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🔒 Lock Allocation"):

            st.session_state.allocation_locked = True

            st.success(
                "Allocations Locked"
            )

    with col2:

        if st.button("🔓 Unlock Allocation"):

            st.session_state.allocation_locked = False

            st.success(
                "Allocations Unlocked"
            )

    st.write(
        "Current Status :",
        "🔒 Locked"
        if st.session_state.allocation_locked
        else "🟢 Open"
    )

    st.divider()

    # ------------------------------------------
    # Market Controls
    # ------------------------------------------

    st.subheader("Market Controls")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⏸ Pause Market"):

            st.session_state.market_locked = True

            st.warning(
                "Market Paused"
            )

    with col2:

        if st.button("▶ Resume Market"):

            st.session_state.market_locked = False

            st.success(
                "Market Active"
            )

    st.write(
        "Market Status :",
        "⏸ Paused"
        if st.session_state.market_locked
        else "▶ Running"
    )

    st.divider()

    # ------------------------------------------
    # End Simulation
    # ------------------------------------------

    st.subheader("Simulation")

    if st.button("🏁 Finish Simulation"):

        st.session_state.game_finished = True

        st.success(
            "Simulation Completed"
        )

    st.divider()

    # ------------------------------------------
    # Portfolio Summary
    # ------------------------------------------

    st.subheader("Current Portfolio Values")

    df = pd.DataFrame({

        "Team":
        st.session_state.team_names,

        "Portfolio Value":[

            st.session_state.portfolio_value[t]

            for t in
            st.session_state.team_names

        ]

    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ------------------------------------------
    # Current Market
    # ------------------------------------------

    st.subheader("Latest Market Scenario")

    if st.session_state.current_market:

        st.info(
            st.session_state.current_market
        )

    else:

        st.warning(
            "No market has been run yet."
        )

    st.divider()

    # ------------------------------------------
    # Reset Simulation
    # ------------------------------------------

    st.subheader("Danger Zone")

    confirm = st.checkbox(
        "I understand this will erase everything."
    )

    if confirm:

        if st.button("🔄 Reset Simulation"):

            keys = list(
                st.session_state.keys()
            )

            for k in keys:

                del st.session_state[k]

            st.rerun()

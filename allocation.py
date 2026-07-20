import streamlit as st
import pandas as pd

from config import (
    ASSETS
)


def allocation_page():

    st.header("📂 Portfolio Allocation")

    st.write(
        """
Each team must allocate **100%** across the four asset classes.

Allocation changes will be used in the next market iteration.
"""
    )

    if st.session_state.allocation_locked:

        st.warning(
            "🔒 Allocations are locked by the teacher."
        )

    allocation_data = []

    # ---------------------------------------------------
    # Input Table
    # ---------------------------------------------------

    for team in st.session_state.team_names:

        current = st.session_state.allocations[team]

        st.subheader(team)

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            equity = st.number_input(
                "Equity %",
                min_value=0,
                max_value=100,
                value=int(current["Equity"]),
                key=f"{team}_equity",
                disabled=st.session_state.allocation_locked
            )

        with c2:

            bonds = st.number_input(
                "Bonds %",
                min_value=0,
                max_value=100,
                value=int(current["Bonds"]),
                key=f"{team}_bonds",
                disabled=st.session_state.allocation_locked
            )

        with c3:

            gold = st.number_input(
                "Gold %",
                min_value=0,
                max_value=100,
                value=int(current["Gold"]),
                key=f"{team}_gold",
                disabled=st.session_state.allocation_locked
            )

        with c4:

            cash = st.number_input(
                "Cash %",
                min_value=0,
                max_value=100,
                value=int(current["Cash"]),
                key=f"{team}_cash",
                disabled=st.session_state.allocation_locked
            )

        total = equity + bonds + gold + cash

        if total == 100:

            st.success("✅ Allocation = 100%")

        else:

            st.error(
                f"Allocation = {total}% (Must equal 100%)"
            )

        allocation_data.append({

            "Team": team,

            "Equity": equity,

            "Bonds": bonds,

            "Gold": gold,

            "Cash": cash,

            "Total": total

        })

        st.divider()

    # ---------------------------------------------------
    # Summary Table
    # ---------------------------------------------------

    df = pd.DataFrame(allocation_data)

    st.subheader("Current Allocations")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # ---------------------------------------------------
    # Save Button
    # ---------------------------------------------------

    if st.button(
        "💾 Save All Teams",
        disabled=st.session_state.allocation_locked
    ):

        valid = True

        for row in allocation_data:

            if row["Total"] != 100:

                valid = False

        if not valid:

            st.error(
                "One or more teams do not total 100%."
            )

            return

        # Save all allocations

        for row in allocation_data:

            team = row["Team"]

            st.session_state.previous_allocations[
                team
            ] = st.session_state.allocations[
                team
            ].copy()

            st.session_state.allocations[
                team
            ] = {

                "Equity": row["Equity"],

                "Bonds": row["Bonds"],

                "Gold": row["Gold"],

                "Cash": row["Cash"]

            }

        st.success(
            "✅ All allocations saved successfully."
        )

        st.balloons()

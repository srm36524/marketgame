import streamlit as st
import pandas as pd

from config import (
    ASSETS
)


def allocation_page():

    st.header("Portfolio Allocation")

    st.info(
        "Each team must allocate exactly 100%."
    )

    if st.session_state.allocation_locked:

        st.warning(
            "Allocations are locked by the teacher."
        )

    summary = []

    for team in st.session_state.team_names:

        st.markdown(f"## {team}")

        old = st.session_state.allocations[team]

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            equity = st.number_input(
                "Equity %",
                min_value=0,
                max_value=100,
                value=int(old["Equity"]),
                key=f"{team}_equity",
                disabled=st.session_state.allocation_locked
            )

        with c2:

            bonds = st.number_input(
                "Bonds %",
                min_value=0,
                max_value=100,
                value=int(old["Bonds"]),
                key=f"{team}_bonds",
                disabled=st.session_state.allocation_locked
            )

        with c3:

            gold = st.number_input(
                "Gold %",
                min_value=0,
                max_value=100,
                value=int(old["Gold"]),
                key=f"{team}_gold",
                disabled=st.session_state.allocation_locked
            )

        with c4:

            cash = st.number_input(
                "Cash %",
                min_value=0,
                max_value=100,
                value=int(old["Cash"]),
                key=f"{team}_cash",
                disabled=st.session_state.allocation_locked
            )

        allocation = {

            "Equity": equity,
            "Bonds": bonds,
            "Gold": gold,
            "Cash": cash

        }

        total = sum(allocation.values())

        if total == 100:

            st.success("Allocation = 100%")

        else:

            st.error(
                f"Allocation = {total}%"
            )

        if st.button(
            f"Save {team}",
            key=f"save_{team}",
            disabled=st.session_state.allocation_locked
        ):

            if total != 100:

                st.error(
                    "Allocation must total 100%."
                )

            else:

                st.session_state.previous_allocations[
                    team
                ] = st.session_state.allocations[
                    team
                ].copy()

                st.session_state.allocations[
                    team
                ] = allocation

                st.success(
                    "Allocation Saved."
                )

        row = {

            "Team": team,

            "Equity": allocation["Equity"],

            "Bonds": allocation["Bonds"],

            "Gold": allocation["Gold"],

            "Cash": allocation["Cash"]

        }

        summary.append(row)

        st.divider()

    st.subheader("Current Allocation Summary")

    df = pd.DataFrame(summary)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

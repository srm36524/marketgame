# =====================================================
# STREAMLIT PAGE SETTINGS
# =====================================================

PAGE_TITLE = "Portfolio Management Simulator"
PAGE_ICON = "📈"
LAYOUT = "wide"

# =====================================================
# SIMULATION SETTINGS
# =====================================================

NUM_TEAMS = 5
NUM_ITERATIONS = 10

INITIAL_CAPITAL = 1_000_000

TRANSACTION_COST = 0.005      # 0.5%
RISK_FREE_RATE = 0.06

# =====================================================
# TEAM NAMES
# =====================================================

TEAM_NAMES = [
    "Alpha",
    "Bravo",
    "Charlie",
    "Delta",
    "Echo"
]

# =====================================================
# ASSETS
# =====================================================

ASSETS = [
    "Equity",
    "Bonds",
    "Gold",
    "Cash"
]

# =====================================================
# DEFAULT ALLOCATION
# =====================================================

DEFAULT_ALLOCATION = {
    "Equity":25,
    "Bonds":25,
    "Gold":25,
    "Cash":25
}

# =====================================================
# MARKET SCENARIOS
# price  = Capital Appreciation
# income = Dividend / Interest
# =====================================================

MARKET_SCENARIOS = {

    "Bull Market":{

        "Equity":{
            "price":0.15,
            "income":0.02
        },

        "Bonds":{
            "price":0.01,
            "income":0.06
        },

        "Gold":{
            "price":-0.02,
            "income":0.00
        },

        "Cash":{
            "price":0.00,
            "income":0.04
        }

    },

    "Bear Market":{

        "Equity":{
            "price":-0.12,
            "income":0.02
        },

        "Bonds":{
            "price":0.04,
            "income":0.06
        },

        "Gold":{
            "price":0.10,
            "income":0.00
        },

        "Cash":{
            "price":0.00,
            "income":0.04
        }

    },

    "Inflation":{

        "Equity":{
            "price":-0.05,
            "income":0.02
        },

        "Bonds":{
            "price":-0.06,
            "income":0.07
        },

        "Gold":{
            "price":0.18,
            "income":0.00
        },

        "Cash":{
            "price":0.00,
            "income":0.05
        }

    },

    "Stable Economy":{

        "Equity":{
            "price":0.06,
            "income":0.02
        },

        "Bonds":{
            "price":0.02,
            "income":0.06
        },

        "Gold":{
            "price":0.03,
            "income":0.00
        },

        "Cash":{
            "price":0.00,
            "income":0.04
        }

    },

    "Tech Boom":{

        "Equity":{
            "price":0.20,
            "income":0.01
        },

        "Bonds":{
            "price":-0.01,
            "income":0.06
        },

        "Gold":{
            "price":-0.05,
            "income":0.00
        },

        "Cash":{
            "price":0.00,
            "income":0.04
        }

    },

    "Market Crash":{

        "Equity":{
            "price":-0.25,
            "income":0.02
        },

        "Bonds":{
            "price":0.08,
            "income":0.06
        },

        "Gold":{
            "price":0.15,
            "income":0.00
        },

        "Cash":{
            "price":0.00,
            "income":0.04
        }

    },

    "Gold Rally":{

        "Equity":{
            "price":0.01,
            "income":0.02
        },

        "Bonds":{
            "price":0.02,
            "income":0.06
        },

        "Gold":{
            "price":0.22,
            "income":0.00
        },

        "Cash":{
            "price":0.00,
            "income":0.04
        }

    }

}

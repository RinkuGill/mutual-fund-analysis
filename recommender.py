import pandas as pd

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

def recommend_funds(risk):

    temp = performance[
        performance["risk_grade"]
        .str.contains(
            risk,
            case=False,
            na=False
        )
    ]

    temp = temp.sort_values(
        "sharpe_ratio",
        ascending=False
    )

    return temp[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio"
        ]
    ].head(3)


print("Moderate Risk Funds")
print(recommend_funds("Moderate"))
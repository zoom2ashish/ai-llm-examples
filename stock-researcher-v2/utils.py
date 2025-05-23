import re

def format_stock_info(info: dict) -> str:
    if not info:
        return "No stock information available."

    return dict_to_pretty_string(info)

    # keys_of_interest = [
    #     "shortName", "symbol", "currentPrice", "marketCap",
    #     "trailingPE", "forwardPE", "dividendYield", "fiftyTwoWeekHigh",
    #     "fiftyTwoWeekLow", "sector", "industry", "website", "longBusinessSummary"
    # ]

    # lines = []
    # for key in keys_of_interest:
    #     value = info.get(key, "N/A")
    #     # Escape brackets and ensure links are Markdown safe
    #     if key == "website" and isinstance(value, str) and value.startswith("http"):
    #         value = f"[{value}]({value})"
    #     lines.append(f"**{key.replace('_', ' ').title()}**: {value}")

    # return "\n\n".join(lines)


def camel_case_to_title(s):
    # Insert space before capital letters and capitalize each word
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s).title()

def dict_to_pretty_string(d):
    lines = [f"**{camel_case_to_title(k)}**: {v}" for k, v in d.items()]
    return "\n".join(lines)

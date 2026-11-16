private void HumanSummary()
{
    string key = GetKey();
    string summary = humanClient.GetSummary(key);
    StartCoroutine(Wait(summary));
}
//using a wait to mask the difference between the ai and human one so testers arent biased
private IEnumerator Wait(string summary)
{
    yield return new WaitForSeconds(1);
    StartCoroutine(SendToUI(summary));
}

private string GetKey()
{
    // 1. Handle the empty case first
    if (events == null || events.Count == 0 || events[0] == null)
    {
        return "NONE";
    }
    List<string> keyParts = new List<string>();
    foreach (var evt in events)
    {
        if (evt == null) continue;
        // Ensure the role starts with a Capital letter (Guard, Merchant, Peasant)
        string role = char.ToUpper(evt.role[0]) + evt.role.Substring(1);
        // Match the CSV casing exactly: _Talk or _Kill
        string action = "";
        if (evt.action == "talked") action = "_Talk";
        else if (evt.action == "killed") action = "_Kill";
        keyParts.Add(role + action);
    }
    // This joins them with '-' only if there are multiple parts
    // e.g., "Guard_Talk-Merchant_Kill"
    return string.Join("-", keyParts);
}

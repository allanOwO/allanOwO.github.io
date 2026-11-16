// Update(): every attack's score climbs at its own randomised rate
for (int i =0; i < scores.Count; i++)
{
    scores[i] += UnityEngine.Random.Range(attackWeights[i][0]/attackRandomness, attackWeights[i][1]*attackRandomness) * Time.deltaTime;
}

// AttackLoop(): the highest score attacks next, then starts again from zero
int choice = FindMax();
yield return new WaitForSeconds(UnityEngine.Random.Range(1, 4));
// ... start the chosen attack ...
scores[choice] = 0;

private int FindMax()
{
    float max = scores[0];
    int position = 0;
    int i = 0;
    foreach(float num in scores)
    {
        if (num > max) { max = num; position = i; }
        i++;
    }
    return position;
}

// StartStageTwo(): force the eye attack first, then make it more likely from here on
scores[5] = 10000;//whichever score is here will attack first after stage 2, in this instance its the eye attack
attackWeights[5][0] = 0.85f;
attackWeights[5][1] = 1.1f;//increases chances off certain attack, here eye attack

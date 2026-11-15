private void Update()
{
    if (path != null && target != null && Time.time - lastUpdateTime > updateInterval)//checks position on a fixed time rather than every frame
    {
        lastUpdateTime = Time.time;
        //get target
        float target = UpdateDollyPosition();

        float pathLength = path.PathLength; // Get the total track length
        float currentPos = dollyCart.m_Position; // Current position of the dolly cart
        float diff = target - currentPos; // Difference between target and current position

        // Ensure shortest path around the loop
        if (Mathf.Abs(diff) > pathLength * 0.5f)
        {
            if (diff > 0)
                diff -= pathLength; // Adjust forward jump if it's too large
            else
                diff += pathLength; // Adjust backward jump if it's too large
        }

        //ensure position wraps within the valid range [0, pathLength]
        float updatedPos = Mathf.Lerp(currentPos, WrapPosition(currentPos + diff), smoothSpeed * Time.deltaTime);
        dollyCart.m_Position = updatedPos;
    }
}

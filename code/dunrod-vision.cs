private bool DetectTarget(Transform target)
{
    Vector3 targetDirection = (target.position - transform.position).normalized;
    float sqrDis = (transform.position - target.position).sqrMagnitude;

    if (sqrDis < viewRange)
    {
        //in view cone?
        Vector3 dirNormalised = (target.position - transform.position).normalized;
        float dot = Vector3.Dot(transform.forward, dirNormalised);//cos() between guard.fwd and target
        bool withinAngle = dot >= cosThreshold;

        bool withinNearDistance = sqrDis <= nearDis;//in near circle?

        if (withinAngle || withinNearDistance)
        {
            float realDis = Mathf.Sqrt(sqrDis);
            if (Physics.Raycast(transform.position, targetDirection, out RaycastHit hit, realDis))
            {
                if (hit.collider.CompareTag(target.tag))//checks if hit target contains player or cheese tag
                {
                    return true;
                }
            }
        }
    }
    return false;
}

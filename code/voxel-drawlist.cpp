for (const VisibleSection& entry : visibleSections) {
    // A face pointing +X can only be seen from its +X side. Every +X face in this mesh is at or past min.x,
    // so with the viewer at or before min.x none of them can be: the whole group is skipped
    // From the sun every face in a group points the same way relative to it, so it's all or nothing
    bool visible[faceGroupCount];
    if (viewPoint) {
        visible[NegXFaces] = viewPoint->x < entry.max.x;
        visible[PosXFaces] = viewPoint->x > entry.min.x;
        visible[NegZFaces] = viewPoint->z < entry.max.y;
        visible[PosZFaces] = viewPoint->z > entry.min.y;
    }
    else {
        visible[NegXFaces] = viewDirection.x > 0.0f;//a -X face faces the viewer when the viewer looks along +X
        visible[PosXFaces] = viewDirection.x < 0.0f;
        visible[NegZFaces] = viewDirection.z > 0.0f;
        visible[PosZFaces] = viewDirection.z < 0.0f;
    }
    visible[VerticalFaces] = true;

// ...

        GLsizei count = mesh.groupCounts[g];
        if (count == 0) continue;
        if (visible[g]) {
            if (runLength == 0) runStart = groupStart;
            runLength += gap + count;//the hidden groups in between come along
            gap = 0;
        }
        else if (runLength > 0 && gap + count < splitAtLeast) {
            gap += count;//maybe drawn, if another visible group follows
        }
        else {
            addRun();//too much hidden in between, split
            gap = 0;
        }
        groupStart += count;
    }
    addRun();//a hidden gap at the end is just left off
}

// 2. Greedy merge: grow each unclaimed cell into the biggest rectangle of identical cells
for (int b = 0; b < size[v]; b++) {
    for (int a = 0; a < size[u];) {
        uint32_t cell = mask[a + b * size[u]];
        if (cell == 0) { a++; continue; }

        // Grow along u while the cells match
        int width = 1;
        while (a + width < size[u] && mask[a + width + b * size[u]] == cell) {
            width++;
        }

        // Grow along v while every cell in the next row matches
        int height = 1;
        bool rowMatches = true;
        while (b + height < size[v] && rowMatches) {
            for (int k = 0; k < width; k++) {
                if (mask[a + k + (b + height) * size[u]] != cell) { rowMatches = false; break; }
            }
            if (rowMatches) height++;
        }

        // Faces pointing + sit on the far side of the block
        glm::ivec3 origin(0);
        origin[axis] = slice + (direction > 0 ? 1 : 0);
        origin[u] = a;
        origin[v] = b;
        addQuad(mesh, origin * scale, uStep * (width * scale), vStep * (height * scale), direction, face, cell);

        // Claim the cells so they aren't used again
        for (int h = 0; h < height; h++) {
            for (int k = 0; k < width; k++) {
                mask[a + k + (b + h) * size[u]] = 0;
            }
        }
        a += width;
    }
}

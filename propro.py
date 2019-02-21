public static boolean isSquare(List<Point> points){
    if(points == null || points.size() != 4)
        return false;
    int dist1 = sqDistance(points.get(0), points.get(1));
    int dist2 = sqDistance(points.get(0), points.get(2));
    if(dist1 == dist2){ //if neither are the diagonal
        dist2 = sqDistance(points.get(0), points.get(3));
    }
    int s = Math.min(dist1, dist2);
    int d = s * 2;

    for(int i=0;i<points.size;i++){
        for(int j=i+1;j<points.size();j++){
            int dist = sqDistance(points.get(i), points.get(j));
            if(dist != s && dist != d))
                return false;
        }
    }
    return true;
}

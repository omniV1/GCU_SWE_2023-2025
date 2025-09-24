// Owen Lindsey
// Professor Demland, David
// CST-201
// Exercise 2
// This work is my own
using System;

// Represents a point with x and y coordinates
class Point
{
    public double X { get; set; }
    public double Y { get; set; }

    public Point(double x, double y)
    {
        X = x;
        Y = y;
    }
}

// Represents a line segment with two endpoints
class LineSegment
{
    public Point P { get; set; }
    public Point Q { get; set; }

    public LineSegment(Point p, Point q)
    {
        P = p;
        Q = q;
    }
}

class Program
{
    // Calculates the cross product to determine the orientation of three points
    static double CrossProduct(Point a, Point b, Point c)
    {
        return (b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X);
    }

    // Checks if point q lies on the line segment pr
    
    static bool OnSegment(Point p, Point q, Point r)
    {
        return q.X <= Math.Max(p.X, r.X) && q.X >= Math.Min(p.X, r.X) &&
               q.Y <= Math.Max(p.Y, r.Y) && q.Y >= Math.Min(p.Y, r.Y);
    }

    // Determines if two line segments intersect
    static bool DoIntersect(LineSegment seg1, LineSegment seg2)
    {
        // Calculate orientations
        double o1 = CrossProduct(seg1.P, seg1.Q, seg2.P);
        double o2 = CrossProduct(seg1.P, seg1.Q, seg2.Q);
        double o3 = CrossProduct(seg2.P, seg2.Q, seg1.P);
        double o4 = CrossProduct(seg2.P, seg2.Q, seg1.Q);

        // General case: segments intersect if orientations are different
        if (o1 * o2 < 0 && o3 * o4 < 0)
            return true;

        // Special cases: check if endpoints lie on the other segment
        if (o1 == 0 && OnSegment(seg1.P, seg2.P, seg1.Q)) return true;
        if (o2 == 0 && OnSegment(seg1.P, seg2.Q, seg1.Q)) return true;
        if (o3 == 0 && OnSegment(seg2.P, seg1.P, seg2.Q)) return true;
        if (o4 == 0 && OnSegment(seg2.P, seg1.Q, seg2.Q)) return true;

        return false;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Enter the coordinates for the first line segment (P1 and Q1):");
        Point p1 = ReadPoint("P1");
        Point q1 = ReadPoint("Q1");

        Console.WriteLine("Enter the coordinates for the second line segment (P2 and Q2):");
        Point p2 = ReadPoint("P2");
        Point q2 = ReadPoint("Q2");

        LineSegment seg1 = new LineSegment(p1, q1);
        LineSegment seg2 = new LineSegment(p2, q2);

        bool intersect = DoIntersect(seg1, seg2);

        Console.WriteLine(intersect
            ? "The line segments intersect."
            : "The line segments do not intersect.");
    }

    // Reads a point's coordinates from user input
    static Point ReadPoint(string pointName)
    {
        Console.Write($"Enter x-coordinate for {pointName}: ");
        double x = double.Parse(Console.ReadLine());
        Console.Write($"Enter y-coordinate for {pointName}: ");
        double y = double.Parse(Console.ReadLine());
        return new Point(x, y);
    }
}
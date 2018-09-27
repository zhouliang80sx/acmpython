#pragma once
#include <cmath>
#include "Binary_Tree.h"
#include <vector>
#include <queue>
#include <list>
#include <algorithm>
struct Point;
struct  Edge;
class Arc;
class Voronoi_diagram;
//class Event {
//	Event() {
//		_place_ = Point();
//	}
//	Event(Point place) {
//		_place_ = place;
//	}
//	const Point& getPlace() {
//		return _place_;
//	}
//	bool operator>(Event eventb) {
//		return (_place_ > eventb.getPlace());
//	}
//	bool operator<(Event eventb) {
//		return _place_ < eventb.getPlace();
//	}
//protected:
//	Point _place_;
//};
//
//class Event_Place : public Event {
//public:
//	Event_Place(Point place) : Event(place) {}
//	const Point& getPlace() : getPlace() {};
//	Event_Place& operator=(Event_Place pl) {
//		_place_ = pl.getPlace();
//		return *this;
//	}
//};
//
//class Event_Circle : public Event {
//public:
//	Event_Circle(Point place, Arc* dissArc) : Event(place) {
//		dissaperingArc = dissArc;
//	}
//
//	const Point& getPlace() : getPlace() {};
//	void deleteArc() {
//		if (dissaperingArc != nullptr)
//		{
//			delete dissaperingArc;
//		}
//	}
//private:
//	Arc * dissaperingArc;
//};


struct Point {
	double x = 0;
	double y = 0;

	// Euclidian distance
	double dist(const Point& b) {
		return sqrt((x - b.x)*(x - b.x) + (y - b.y)*(y - b.y));
	}

	Point& operator=(Point b) {
		x = b.x;
		y = b.y;
		return *this;
	}

	bool operator==(const Point& b) {
		return x == b.x && y == b.y;
	}

	bool operator>(const Point& b) {
		return (y > b.y) || (y <= b.y && x > b.x);
	}

	bool operator<(const Point& b) {
		return (y < b.y) || (y >= b.y && x < b.x);
	}
};

struct  Edge
{
	Point a;
	Point b;

	double length() {
		return a.dist(b);
	}
};

class Arc {
public:
	Arc(Point pi) {
		p = pi;
	}

	Point getP() {
		return p;
	}

	double Bi(double ly, double x) {
		return (x - p.x)*(x - p.x) * 0.5 / (p.y - ly) + (p.y + ly) * 0.5;
	}

	bool operator>(Arc b) {
		return p > b.getP();
	}

	bool operator<(Arc b) {
		return p < b.getP();
	}
private:
	Point p;
};


class Voronoi_diagram{
public:
	class Event;
	Voronoi_diagram();
	Voronoi_diagram(std::vector<Point> P);
	void setNewPoints(std::vector<Point> P);

private:
	class Event {
	public:
		struct Circle_Event;

		Event() {
			isPlace = false;
			isCircle = false;
		}


		Event(Point p) {
			isPlace = true;
			isCircle = false;
			Place = p;
			_circle = Circle_Event();
		}


		Event(Point p, Arc* dissArc) {
			isPlace = false;
			isCircle = true;
			Place = p;
			_circle.dissaperingArc = dissArc;
		}


		bool isPlace_Event() {
			return isPlace;
		}

		bool operator>(Event b) {
			return Place > b.getPlace();
		}

		bool operator<(Event b) {
			return Place < b.getPlace();
		}

		bool operator==(Event b) {
			return Place == b.getPlace();
		}

		Point getPlace() {
			return Place;
		}

		Event& operator=(Event ev) {
			isPlace = ev.isPlace_Event();
			isCircle = !isPlace;
			Place = ev.getPlace();
			_circle = ev.getCircleEvent();
			return *this;
		}
	private:
		struct Circle_Event {
			Arc* dissaperingArc;
			Circle_Event() {
				dissaperingArc = nullptr;
			}

			Circle_Event& operator=(Circle_Event cir) {
				dissaperingArc = cir.dissaperingArc;
				return *this;
			}
		};

		Circle_Event getCircleEvent() {
			if (isCircle)
				return _circle;
			return Circle_Event();
		}

		bool isPlace;
		Circle_Event _circle;
		bool isCircle;

		Point Place;
	};

	// std::vector<Point> points;	// P
	std::priority_queue<Event> events;	// Q
	std::list<Edge> edges;		// D
	Binary_Tree<Arc> beachLine;	// T

	void HandlePlaceEvent(Event p);
	void HandleCircleEvent(Event p);

	void ConstructDiagram();
};
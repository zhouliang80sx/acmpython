#include "Voronoi_Diagram.h"
using namespace std;
class Event;

Voronoi_diagram::Voronoi_diagram() {};

Voronoi_diagram::Voronoi_diagram(std::vector<Point> P)
{
	setNewPoints(P);
}

void Voronoi_diagram::setNewPoints(std::vector<Point> P)
{
	edges.clear();
	// initialize T
	for (int i = 0; i < P.size(); ++i) {
		events.push(Event(P[i]));
	}
}

void Voronoi_diagram::HandlePlaceEvent(Event p)
{
	if (beachLine.isEmpty()) {
		beachLine.insert(Arc(p.getPlace()));
	}
	else {

	}
}

void Voronoi_diagram::ConstructDiagram()
{
	Event currentEvent;
	while (!events.empty())
	{
		currentEvent = events.top();
		events.pop();
		if (currentEvent.isPlace_Event()) {
			HandlePlaceEvent(currentEvent);
		}
		else {
			HandleCircleEvent(currentEvent);
		}
	}
}
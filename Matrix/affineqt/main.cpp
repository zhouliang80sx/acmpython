#include "xform.h"

#include <QApplication>

int main(int argc, char **argv)
{
    Q_INIT_RESOURCE(affine);

    QApplication app(argc, argv);

    XFormWidget xformWidget(0);
    QStyle *arthurStyle = new ArthurStyle();
    xformWidget.setStyle(arthurStyle);

    QList<QWidget *> widgets = xformWidget.findChildren<QWidget *>();
    foreach (QWidget *w, widgets) {
        w->setStyle(arthurStyle);
        w->setAttribute(Qt::WA_AcceptTouchEvents);
    }

    xformWidget.show();

    return app.exec();
}
#ifndef XFORM_H
#define XFORM_H

#include "arthurwidgets.h"

#include <QBasicTimer>
#include <QPolygonF>

class HoverPoints;

class QLineEdit;

class XFormView : public ArthurFrame
{
public:
    Q_OBJECT

    Q_PROPERTY(XFormType type READ type WRITE setType)
    Q_PROPERTY(bool animation READ animation WRITE setAnimation)
    Q_PROPERTY(qreal shear READ shear WRITE setShear)
    Q_PROPERTY(qreal rotation READ rotation WRITE setRotation)
    Q_PROPERTY(qreal scale READ scale WRITE setScale)
    Q_PROPERTY(QString text READ text WRITE setText)
    Q_PROPERTY(QPixmap pixmap READ pixmap WRITE setPixmap)
    Q_ENUMS(XFormType)

public:
    enum XFormType { VectorType, PixmapType, TextType };

    XFormView(QWidget *parent);
    void paint(QPainter *) override;
    void drawVectorType(QPainter *painter);
    void drawPixmapType(QPainter *painter);
    void drawTextType(QPainter *painter);
    QSize sizeHint() const override { return QSize(500, 500); }

    void mousePressEvent(QMouseEvent *e) override;
    void resizeEvent(QResizeEvent *e) override;
    HoverPoints *hoverPoints() { return pts; }

    bool animation() const { return timer.isActive(); }
    qreal shear() const { return m_shear; }
    qreal scale() const { return m_scale; }
    qreal rotation() const { return m_rotation; }
    void setShear(qreal s);
    void setScale(qreal s);
    void setRotation(qreal r);

    XFormType type() const;
    QPixmap pixmap() const;
    QString text() const;

public slots:
    void setAnimation(bool animate);
    void updateCtrlPoints(const QPolygonF &);
    void changeRotation(int rotation);
    void changeScale(int scale);
    void changeShear(int shear);

    void setText(const QString &);
    void setPixmap(const QPixmap &);
    void setType(XFormType t);

    void setVectorType();
    void setPixmapType();
    void setTextType();
    void reset();

signals:
    void rotationChanged(int rotation);
    void scaleChanged(int scale);
    void shearChanged(int shear);

protected:
    void timerEvent(QTimerEvent *e) override;
#if QT_CONFIG(wheelevent)
    void wheelEvent(QWheelEvent *) override;
#endif

private:
    QPolygonF ctrlPoints;
    HoverPoints *pts;
    qreal m_rotation;
    qreal m_scale;
    qreal m_shear;
    XFormType m_type;
    QPixmap m_pixmap;
    QString m_text;
    QBasicTimer timer;
};

class XFormWidget : public QWidget
{
    Q_OBJECT
public:
    XFormWidget(QWidget *parent);

private:
    XFormView *view;
    QLineEdit *textEditor;
};

#endif // XFORM_H
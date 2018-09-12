/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout_2;
    QGraphicsView *graphicsView;
    QSlider *hsAnimationParameter;
    QHBoxLayout *navBar;
    QPushButton *btnLoadFile;
    QFrame *line_4;
    QLabel *label;
    QSpinBox *sbNumOfPoints;
    QPushButton *btnGenerate;
    QFrame *line_2;
    QLabel *lblX;
    QDoubleSpinBox *dsbX;
    QLabel *lblY;
    QDoubleSpinBox *dsbY;
    QPushButton *btnAddPoint;
    QSpacerItem *horizontalSpacer;
    QPushButton *btnClear;
    QFrame *line_3;
    QPushButton *btnStart;
    QFrame *line;
    QPushButton *btnPrevious;
    QPushButton *btnNext;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(900, 506);
        MainWindow->setMinimumSize(QSize(900, 300));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        verticalLayout_2 = new QVBoxLayout(centralWidget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        graphicsView = new QGraphicsView(centralWidget);
        graphicsView->setObjectName(QStringLiteral("graphicsView"));
        graphicsView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        graphicsView->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

        verticalLayout_2->addWidget(graphicsView);

        hsAnimationParameter = new QSlider(centralWidget);
        hsAnimationParameter->setObjectName(QStringLiteral("hsAnimationParameter"));
        hsAnimationParameter->setMaximum(100000);
        hsAnimationParameter->setSingleStep(1);
        hsAnimationParameter->setOrientation(Qt::Horizontal);

        verticalLayout_2->addWidget(hsAnimationParameter);

        navBar = new QHBoxLayout();
        navBar->setSpacing(6);
        navBar->setObjectName(QStringLiteral("navBar"));
        btnLoadFile = new QPushButton(centralWidget);
        btnLoadFile->setObjectName(QStringLiteral("btnLoadFile"));

        navBar->addWidget(btnLoadFile);

        line_4 = new QFrame(centralWidget);
        line_4->setObjectName(QStringLiteral("line_4"));
        line_4->setFrameShape(QFrame::VLine);
        line_4->setFrameShadow(QFrame::Sunken);

        navBar->addWidget(line_4);

        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));

        navBar->addWidget(label);

        sbNumOfPoints = new QSpinBox(centralWidget);
        sbNumOfPoints->setObjectName(QStringLiteral("sbNumOfPoints"));
        sbNumOfPoints->setMinimum(3);
        sbNumOfPoints->setMaximum(100);
        sbNumOfPoints->setValue(50);

        navBar->addWidget(sbNumOfPoints);

        btnGenerate = new QPushButton(centralWidget);
        btnGenerate->setObjectName(QStringLiteral("btnGenerate"));

        navBar->addWidget(btnGenerate);

        line_2 = new QFrame(centralWidget);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);

        navBar->addWidget(line_2);

        lblX = new QLabel(centralWidget);
        lblX->setObjectName(QStringLiteral("lblX"));

        navBar->addWidget(lblX);

        dsbX = new QDoubleSpinBox(centralWidget);
        dsbX->setObjectName(QStringLiteral("dsbX"));

        navBar->addWidget(dsbX);

        lblY = new QLabel(centralWidget);
        lblY->setObjectName(QStringLiteral("lblY"));

        navBar->addWidget(lblY);

        dsbY = new QDoubleSpinBox(centralWidget);
        dsbY->setObjectName(QStringLiteral("dsbY"));

        navBar->addWidget(dsbY);

        btnAddPoint = new QPushButton(centralWidget);
        btnAddPoint->setObjectName(QStringLiteral("btnAddPoint"));

        navBar->addWidget(btnAddPoint);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        navBar->addItem(horizontalSpacer);

        btnClear = new QPushButton(centralWidget);
        btnClear->setObjectName(QStringLiteral("btnClear"));

        navBar->addWidget(btnClear);

        line_3 = new QFrame(centralWidget);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setFrameShape(QFrame::VLine);
        line_3->setFrameShadow(QFrame::Sunken);

        navBar->addWidget(line_3);

        btnStart = new QPushButton(centralWidget);
        btnStart->setObjectName(QStringLiteral("btnStart"));

        navBar->addWidget(btnStart);

        line = new QFrame(centralWidget);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        navBar->addWidget(line);

        btnPrevious = new QPushButton(centralWidget);
        btnPrevious->setObjectName(QStringLiteral("btnPrevious"));

        navBar->addWidget(btnPrevious);

        btnNext = new QPushButton(centralWidget);
        btnNext->setObjectName(QStringLiteral("btnNext"));

        navBar->addWidget(btnNext);


        verticalLayout_2->addLayout(navBar);

        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Visualisation of Fortune's algorithm (Voronoi diagram)", nullptr));
        btnLoadFile->setText(QApplication::translate("MainWindow", "Load file", nullptr));
        label->setText(QApplication::translate("MainWindow", "Count:", nullptr));
        btnGenerate->setText(QApplication::translate("MainWindow", "Generate", nullptr));
        lblX->setText(QApplication::translate("MainWindow", "X:", nullptr));
        lblY->setText(QApplication::translate("MainWindow", "Y:", nullptr));
        btnAddPoint->setText(QApplication::translate("MainWindow", "Add point", nullptr));
        btnClear->setText(QApplication::translate("MainWindow", "Clear", nullptr));
        btnStart->setText(QApplication::translate("MainWindow", "Start", nullptr));
        btnPrevious->setText(QApplication::translate("MainWindow", "Previous", nullptr));
        btnNext->setText(QApplication::translate("MainWindow", "Next", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H

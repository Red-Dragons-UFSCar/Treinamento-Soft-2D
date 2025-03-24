#include <iostream>
#include <tuple>
#include <cmath> 

class Robot {
private:
    double xPos;   
    double yPos;   
    double theta;  
    double L;      
    double R;      

public:
    Robot() : xPos(0.0), yPos(0.0), theta(0.0), L(7.5), R(3.5) {}

    double getXPos() const { return xPos; }
    void setXPos(double x) { xPos = x; }
    double getYPos() const { return yPos; }
    void setYPos(double y) { yPos = y; }
    double getTheta() const { return theta; }
    void setTheta(double t) { theta = t; }
    double getL() const { return L; }
    void setL(double l) { L = l; }
    double getR() const { return R; }
    void setR(double r) { R = r; }
    void setPose(double x, double y, double t) {
        xPos = x;
        yPos = y;
        theta = t;
    }
};

class Ball {
private:
    double xPos;   
    double yPos;   

public:
    Ball() : xPos(0.0), yPos(0.0) {}

    double getXPos() const { return xPos; }
    void setXPos(double x) { xPos = x; }
    double getYPos() const { return yPos; }
    void setYPos(double y) { yPos = y; }
    void setPose(double x, double y) {
        xPos = x;
        yPos = y;
    }
};

class Vision {
public:
    std::tuple<double, double, double> getPoseRobot() const {
        
        double x = 75.0;    
        double y = 65.0;    
        double theta = 0.0;
        return std::make_tuple(x, y, theta);
    }

    std::tuple<double, double> getPoseBall() const {
        double x = 75.0;   
        double y = 65.0;    
        return std::make_tuple(x, y);
    }
};

int main() {
    Robot robot;
    Ball ball;
    Vision vision;

    robot.setPose(10.0, 20.0, 1.57);
    std::cout << "Pose do Robô: (" << robot.getXPos() << ", " << robot.getYPos() 
              << ", " << robot.getTheta() << ")\n";

    ball.setPose(50.0, 60.0);
    std::cout << "Pose da Bola: (" << ball.getXPos() << ", " << ball.getYPos() << ")\n";

    auto robotPose = vision.getPoseRobot();
    std::cout << "Pose do Robô (Visão): (" << std::get<0>(robotPose) << ", " 
              << std::get<1>(robotPose) << ", " << std::get<2>(robotPose) << ")\n";

    auto ballPose = vision.getPoseBall();
    std::cout << "Pose da Bola (Visão): (" << std::get<0>(ballPose) << ", " 
              << std::get<1>(ballPose) << ")\n";

    return 0;
}
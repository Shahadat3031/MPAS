//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2003 Ahmet Sekercioglu
// Copyright (C) 2003-2008 Andras Varga
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

#include <string.h>
#include <omnetpp.h>


/**
 * In this class we add some debug messages to Txc1. When you run the
 * simulation in the OMNeT++ GUI Tkenv, the output will appear in
 * the main text window, and you can also open separate output windows
 * for `tic' and `toc'.
 */
class Txc2 : public cSimpleModule
{
  protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg);
};

Define_Module(Txc2);

void Txc2::initialize()
{
    if (strcmp("tic", getName()) == 0)
    {
        // The `ev' object works like `cout' in C++.
        EV << "Here we go\n";
        cMessage *msg = new cMessage("trololol");
        send(msg, "out");
    }
}

void Txc2::handleMessage(cMessage *msg)
{
    // msg->getName() is name of the msg object, here it will be "tictocMsg".
    EV << "Received message `" << msg->getName() << "', aaaaand ... its gone\n";
    send(msg, "out");
}


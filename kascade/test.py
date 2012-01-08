from __future__ import division

import tables
import time

from sapphire.analysis import process_events


N = 1000


def show_processing_time(events, dt, limit):
    if limit:
        guess_dt = len(events) / limit * dt
    else:
        guess_dt = dt
        limit = len(events)
    print "Processing %d events: %.2f s" % (limit, dt)
    print "Estimate for total processing time: %.2f h" % (guess_dt / 3600)


if __name__ == '__main__':
    try:
        data
    except NameError:
        data = tables.openFile('kascade.h5', 'r')

    cls = process_events.ProcessEvents(
                data, '/hisparc/cluster_kascade/station_601', limit=N)

    t0 = time.time()
    ts = cls.process_traces()
    dt = time.time() - t0
    show_processing_time(data.root.hisparc.cluster_kascade.station_601.events,
                         dt, N)


    indexes = data.root.kascade.c_index[:,1][:N]
    cls = process_events.ProcessIndexedEvents(
                data, '/hisparc/cluster_kascade/station_601', indexes)
    t0 = time.time()
    ts = cls.process_traces()
    dt = time.time() - t0
    show_processing_time(data.root.kascade.c_index, dt, N)

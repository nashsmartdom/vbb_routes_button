# VBB Routes Button

Separate Home Assistant custom integration for manual VBB/BVG route queries.

This integration is independent from `vbb_routes` and uses the separate domain:

```text
vbb_routes_button
```

## Purpose

Unlike the normal VBB Routes integration, this one does not poll periodically. It creates:

- one refresh button
- route sensors

The route sensors update only after pressing the refresh button.

## Installation via HACS

1. HACS → Custom repositories
2. Add:

```text
https://github.com/nashsmartdom/vbb_routes_button
```

3. Category: Integration
4. Download
5. Restart Home Assistant
6. Settings → Devices & services → Add integration → VBB Routes Button

## Entities

Example entity names:

```text
button.vbb_button_pankow_refresh
sensor.vbb_button_pankow_route_1
sensor.vbb_button_pankow_route_2
sensor.vbb_button_pankow_route_3
```

Pressing the button calls VBB and updates the route sensors.

## Lovelace example

```yaml
type: vertical-stack
cards:
  - type: button
    entity: button.vbb_button_pankow_refresh
    name: VBB aktualisieren
    icon: mdi:refresh
    tap_action:
      action: call-service
      service: button.press
      target:
        entity_id: button.vbb_button_pankow_refresh

  - type: custom:vbb-routes-card
    title: VBB Pankow manuell
    origin: Karl-Marx-Allee 72
    destination: S+U Pankow
    entities:
      - sensor.vbb_button_pankow_route_1
      - sensor.vbb_button_pankow_route_2
      - sensor.vbb_button_pankow_route_3
    maxRoutes: 3
    maxTransfers: 1
    hideMultiTransfer: true
```

## Data source

<https://v6.vbb.transport.rest>

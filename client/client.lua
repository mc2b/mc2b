local isWatchOpen = false
local playerStatus = {
    hunger = 100.0,
    thirst = 100.0,
    hygiene = 100.0,
    radioactivity = 0.0,
    infection = 0.0
}

-- Thread for handling stat updates (every second)
Citizen.CreateThread(function()
    while true do
        Citizen.Wait(1000)

        local ped = PlayerPedId()

        -- Prevent updates if player doesn't exist yet
        if not DoesEntityExist(ped) then
            Citizen.Wait(1000)
        else
            local health = (GetEntityHealth(ped) - 100)
            local armor = GetPedArmour(ped)
            local stamina = 100 -- Placeholder, as reliable stamina native is tricky

            -- Simulate decay (replace with your framework's logic)
            if playerStatus.hunger > 0 then playerStatus.hunger = playerStatus.hunger - 0.1 end
            if playerStatus.thirst > 0 then playerStatus.thirst = playerStatus.thirst - 0.2 end

            -- Send data to UI
            SendNUIMessage({
                action = 'updateHud',
                stats = {
                    health = health,
                    armor = armor,
                    stamina = stamina,
                    hunger = playerStatus.hunger,
                    thirst = playerStatus.thirst,
                    hygiene = playerStatus.hygiene,
                    radioactivity = playerStatus.radioactivity,
                    infection = playerStatus.infection
                }
            })
        end
    end
end)

-- Thread for handling player input and animations (every frame)
Citizen.CreateThread(function()
    local animDict = "amb@world_human_wrist_watch@male@male_a"

    -- Request the animation dictionary
    RequestAnimDict(animDict)
    while not HasAnimDictLoaded(animDict) do
        Citizen.Wait(100)
    end

    while true do
        Citizen.Wait(0)
        local ped = PlayerPedId()

        -- Check if the player presses the key (U on keyboard)
        if IsControlJustPressed(0, 73) and not IsPedInAnyVehicle(ped, false) then -- 73 = INPUT_REPLAY_SHOWHOTKEY
            isWatchOpen = not isWatchOpen

            if isWatchOpen then
                -- Show watch
                SendNUIMessage({ action = 'show' })
                TaskPlayAnim(ped, animDict, "base", 8.0, -8.0, -1, 49, 0, false, false, false)
            else
                -- Hide watch
                ClearPedTasks(ped)
                SendNUIMessage({ action = 'hide' })
            end
        end

        -- Auto-close watch if player starts shooting, sprinting, or enters a vehicle
        if isWatchOpen and (IsPedShooting(ped) or IsPedSprinting(ped) or IsPedInAnyVehicle(ped, false)) then
            isWatchOpen = false
            ClearPedTasks(ped)
            SendNUIMessage({ action = 'hide' })
        end
    end
end)

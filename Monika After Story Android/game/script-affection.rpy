











































init python:



    mas_curr_affection = store.mas_affection.NORMAL
    mas_curr_affection_group = store.mas_affection.G_NORMAL


init -900 python in mas_affection:
    import binascii
    import random
    import base64
    import collections
    import datetime
    import struct
    import time

    import store
    from store import (
        persistent,
        mas_utils
    )

    _m1_script0x2daffection__is_dirty = False



    BROKEN = 1
    DISTRESSED = 2
    UPSET = 3
    NORMAL = 4
    HAPPY = 5
    AFFECTIONATE = 6
    ENAMORED = 7
    LOVE = 8


    _aff_order = [
        BROKEN,
        DISTRESSED,
        UPSET,
        NORMAL,
        HAPPY,
        AFFECTIONATE,
        ENAMORED,
        LOVE
    ]


    _aff_level_map = {}
    for _item in _aff_order:
        _aff_level_map[_item] = _item



    _aff_cascade_map = {
        BROKEN: DISTRESSED,
        DISTRESSED: UPSET,
        UPSET: NORMAL,
        HAPPY: NORMAL,
        AFFECTIONATE: HAPPY,
        ENAMORED: AFFECTIONATE,
        LOVE: ENAMORED
    }

    _m1_script0x2daffection__BACKUP_SENTRY = object()
    _m1_script0x2daffection__runtime_backup = _m1_script0x2daffection__BACKUP_SENTRY


    G_SAD = -1
    G_HAPPY = -2
    G_NORMAL = -3


    _affg_order = [
        G_SAD,
        G_NORMAL,
        G_HAPPY
    ]



    _affg_cascade_map = {
        G_SAD: G_NORMAL,
        G_HAPPY: G_NORMAL
    }


    FORCE_EXP_MAP = {
        BROKEN: "monika 6ckc_static",
        DISTRESSED: "monika 6rkc_static",
        UPSET: "monika 2esc_static",
        NORMAL: "monika 1eua_static",
        AFFECTIONATE: "monika 1eua_static",
        ENAMORED: "monika 1hua_static",
        LOVE: "monika 1hua_static",
    }

    _m1_script0x2daffection__STRUCT_FMT = "!d d d d d d d"
    _m1_script0x2daffection__STRUCT_DEF_VALUES = tuple([0.0] * _m1_script0x2daffection__STRUCT_FMT.count("d"))

    _m1_script0x2daffection__DEF_AFF_GAIN_MAP = {
        BROKEN: 0.25,
        DISTRESSED: 0.5,
        UPSET: 0.75,
        NORMAL: 1.0,
        HAPPY: 1.25,
        AFFECTIONATE: 1.5,
        ENAMORED: 2.5,
        LOVE: 2.0
    }
    _m1_script0x2daffection__DEF_AFF_LOSE_MAP = {
        BROKEN: 20.0,
        DISTRESSED: 15.0,
        UPSET: 10.0,
        NORMAL: 5.0,
        HAPPY: 10.0,
        AFFECTIONATE: 15.0,
        ENAMORED: 30.0,
        LOVE: 60.0
    }
    _m1_script0x2daffection__DEF_AFF_FRACTION_LOSE_MAP = {
        BROKEN: 0.3,
        DISTRESSED: 0.15,
        UPSET: 0.1,
        NORMAL: 0.05,
        HAPPY: 0.1,
        AFFECTIONATE: 0.1,
        ENAMORED: 0.125,
        LOVE: 0.15
    }

    _m1_script0x2daffection__STRUCT = struct.Struct(_m1_script0x2daffection__STRUCT_FMT)


    def _compareAff(aff_1, aff_2):
        """
        See mas_compareAff for explanation
        """
        
        if aff_1 == aff_2:
            return 0
        
        
        if aff_1 not in _aff_order or aff_2 not in _aff_order:
            return 0
        
        
        if _aff_order.index(aff_1) < _aff_order.index(aff_2):
            return -1
        
        return 1


    def _compareAffG(affg_1, affg_2):
        """
        See mas_compareAffG for explanation
        """
        
        if affg_1 == affg_2:
            return 0
        
        
        if affg_1 not in _affg_order or affg_2 not in _affg_order:
            return 0
        
        
        if _affg_order.index(affg_1) < _affg_order.index(affg_2):
            return -1
        
        return 1


    def _betweenAff(aff_low, aff_check, aff_high):
        """
        checks if the given affection level is between the given low and high.
        See mas_betweenAff for explanation
        """
        aff_check = _aff_level_map.get(aff_check, None)
        
        
        if aff_check is None:
            
            return False
        
        
        aff_low = _aff_level_map.get(aff_low, None)
        aff_high = _aff_level_map.get(aff_high, None)
        
        if aff_low is None and aff_high is None:
            
            
            return True
        
        if aff_low is None:
            
            
            return _compareAff(aff_check, aff_high) <= 0
        
        if aff_high is None:
            
            
            return _compareAff(aff_check, aff_low) >= 0
        
        
        
        comp_low_high = _compareAff(aff_low, aff_high)
        if comp_low_high > 0:
            
            
            return False
        
        if comp_low_high == 0:
            
            return _compareAff(aff_low, aff_check) == 0
        
        
        return (
            _compareAff(aff_low, aff_check) <= 0
            and _compareAff(aff_check, aff_high) <= 0
        )


    def _isValidAff(aff_check):
        """
        Returns true if the given affection is a valid affection state

        NOTE: None is considered valid
        """
        if aff_check is None:
            return True
        
        return aff_check in _aff_level_map


    def _isValidAffRange(aff_range):
        """
        Returns True if the given aff range is a valid aff range.

        IN:
            aff_range - tuple of the following format:
                [0]: lower bound
                [1]: upper bound
            NOTE: Nones are considerd valid.
        """
        if aff_range is None:
            return True
        
        low, high = aff_range
        
        if not _isValidAff(low):
            return False
        
        if not _isValidAff(high):
            return False
        
        if low is None and high is None:
            return True
        
        return _compareAff(low, high) <= 0

    def _m1_script0x2daffection__verify_data():
        global _m1_script0x2daffection__runtime_backup
        
        if _m1_script0x2daffection__runtime_backup is _m1_script0x2daffection__BACKUP_SENTRY:
            _m1_script0x2daffection__runtime_backup = persistent._mas_affection_data
        
        elif _m1_script0x2daffection__runtime_backup != persistent._mas_affection_data:
            
            _m1_script0x2daffection__runtime_backup = _m1_script0x2daffection__BACKUP_SENTRY
            log.info("DATA CORRUPTION")
            success = _restore_backup()
            if success:
                _make_backup()
            else:
                _m1_script0x2daffection__runtime_backup = persistent._mas_affection_data = get_default_data()
            
            return False
        
        return True

    def _m1_script0x2daffection__set_pers_data(value):
        global _m1_script0x2daffection__is_dirty, _m1_script0x2daffection__runtime_backup
        
        if not _m1_script0x2daffection__is_dirty:
            log.info("UNEXPECTED DATA CHANGE, SKIPPING")
            return
        
        _m1_script0x2daffection__is_dirty = False
        
        if not isinstance(value, (basestring, bytes)):
            log.info(
                "NEW DATA HAS INVALID TYPE ({}), SKIPPING".format(
                    type(value).__name__
                )
            )
            return
        
        if not _m1_script0x2daffection__verify_data():
            log.info("VERIFICATION FAILED, SKIPPING")
            return
        
        _m1_script0x2daffection__runtime_backup = persistent._mas_affection_data = value
        _make_backup()

    def _m1_script0x2daffection__get_pers_data():
        global _m1_script0x2daffection__runtime_backup
        
        _m1_script0x2daffection__verify_data()
        
        return _m1_script0x2daffection__runtime_backup

    def _m1_script0x2daffection__to_struct(*args):
        """
        Packs passed args into a struct

        IN:
            *args - the arguments to pass into the struct

        OUT:
            PY2:
                str
            PY3:
                bytes
        """
        return _m1_script0x2daffection__STRUCT.pack(*args)

    def _m1_script0x2daffection__from_struct(struct_):
        """
        Upacks passed struct into a tuple of values

        IN:
            struct_ - bytes - the struct to unpack

        OUT:
            tuple with values
        """
        return _m1_script0x2daffection__STRUCT.unpack(struct_)

    def _m1_script0x2daffection__hexlify(bytes_):
        """
        Converts binary data into a hexadecimal string
        """
        return binascii.hexlify(bytes_)

    def _m1_script0x2daffection__unhexlify(bytes_):
        """
        Converts a hexadecimal string into pure binary data
        """
        return binascii.unhexlify(bytes_)

    def _m1_script0x2daffection__handle_str2bytes(value):
        """
        Verifies we return the expected type,
        if not, converts it
        TODO: ME
        """
        return value

    def _m1_script0x2daffection__intob64(bytes_):
        """
        Encodes a string using b64
        """
        return base64.b64encode(bytes_)

    def _m1_script0x2daffection__fromb64(bytes_):
        """
        Decodes an encoded string using b64
        """
        return base64.b64decode(bytes_)

    def _m1_script0x2daffection__decode_data(data):
        """
        Returns decoded data
        In case the data has been corrupted in a way,
            returns default values

        OUT:
            - tuple with the data
            - None if an error happened
        """
        try:
            data = _m1_script0x2daffection__from_struct(
                _m1_script0x2daffection__unhexlify(
                    _m1_script0x2daffection__fromb64(
                        data
                    )
                )
            )
        
        except (binascii.Incomplete, binascii.Error) as e:
            mas_utils.mas_log.error("Failed to convert hex data: {}".format(e))
        
        except struct.error as e:
            mas_utils.mas_log.error("Failed to unpack struct data: {}".format(e))
        
        except Exception as e:
            mas_utils.mas_log.error("Failed to decode data: {}".format(e))
        
        else:
            return data
        
        return None

    def _m1_script0x2daffection__encode_data(*data):
        """
        Encodes data
        If it's unable to encode data, returns None

        OUT:
            - bytes
            - None if an error happened
        """
        try:
            encoded_data = _m1_script0x2daffection__intob64(
                _m1_script0x2daffection__hexlify(
                    _m1_script0x2daffection__to_struct(*data)
                )
            )
        
        except (binascii.Incomplete, binascii.Error) as e:
            mas_utils.mas_log.error("Failed to convert hex data: {}".format(e))
        
        except struct.error as e:
            mas_utils.mas_log.error("Failed to unpack struct data: {}".format(e))
        
        except Exception as e:
            mas_utils.mas_log.error("Failed to encode pers data: {}".format(e))
        
        else:
            return encoded_data
        
        return None

    def get_default_data():
        """
        Returns default encoded data for aff when first loading the mod

        OUT:
            bytes
        """
        return _m1_script0x2daffection__encode_data(*_m1_script0x2daffection__STRUCT_DEF_VALUES)

    def _m1_script0x2daffection__reset_pers_data():
        """
        Resets pers data to the default value
        Dangerous, think twice before using
        """
        global _m1_script0x2daffection__is_dirty
        _m1_script0x2daffection__is_dirty = True
        _m1_script0x2daffection__set_pers_data(get_default_data())

    def _m1_script0x2daffection__get_data():
        """
        Returns current data (decoded),
        ALWAYS use this accessor

        OUT:
            - list with the data
            - None if an error happened
        """
        data = _m1_script0x2daffection__get_pers_data()
        if data is None:
            mas_utils.mas_log.critical("Aff data is invalid")
            return None
        
        data = _m1_script0x2daffection__decode_data(data)
        if data is None:
            mas_utils.mas_log.critical("Failed to decode aff data")
            return None
        
        return list(data)

    def _get_aff():
        """
        Private getter that handles errors,
        you should probably use public version

        OUT:
            float - current affection
        """
        data = _m1_script0x2daffection__get_data()
        if data is None:
            return 0.0
        
        return data[0]

    def _get_today_cap():
        """
        Returns today's aff cap

        OUT:
            tuple[float, float] - current aff cap
        """
        data = _m1_script0x2daffection__get_data()
        if data is None:
            return (0.0, 0.0)
        
        return data[2:4]

    def _m1_script0x2daffection__validate_timestamp(ts, now_ts):
        """
        Verifies the given time against current time

        IN:
            ts - the timestamp to validate
            now_ts - the current time

        OUT:
            float:
                original timestamp if it's valid
                or modified timestamp
        """
        
        delta_t = ts - now_ts
        hour_t = 3600
        day_t = hour_t * 24
        timezone_hop = hour_t * 30
        
        if delta_t > timezone_hop:
            log.info("INVALID TIME, POSSIBLE CORRUPTION")
            penalty = max(min(delta_t, day_t*30), day_t)
            ts = now_ts + penalty
        
        return ts

    def _grant_aff(amount, bypass, reason=None):
        """
        Grants some affection

        IN:
            amount - float - amount of affection to grant
            bypass - bool - is this bypass gain or not
            reason - str/None - the reason for this bonus,
                MUST be current topic label or None
                (Default: None)
        """
        global _m1_script0x2daffection__is_dirty
        
        
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError("Invalid value for affection: {}".format(amount))
        
        data = _m1_script0x2daffection__get_data()
        if not data:
            return
        
        now_ = time.time()
        data[4] = _m1_script0x2daffection__validate_timestamp(data[4], now_)
        
        freeze_date = datetime.date.fromtimestamp(data[4])
        if store.mas_pastOneDay(freeze_date):
            data[2] = 0.0
            data[3] = 0.0
            data[4] = now_
            data[6] = random.triangular(5.0, 8.0)
        
        frozen = data[2] >= data[6]
        
        og_amount = amount
        
        amount = min(amount, 50.0)
        
        
        amount = max(0.0, random.gauss(amount, 0.25))
        
        
        max_gain = max(1000000-data[0], 0.0)
        amount = min(amount, max_gain)
        
        bank_amount = 0.0
        
        if bypass:
            
            bypass_limit = 30.0 if store.mas_isSpecialDay() else 10.0
            bypass_available = max(bypass_limit - data[3], 0.0)
            temp_amount = amount - bypass_available
            
            if temp_amount > 0.0:
                
                bank_available = max(70.0-data[1], 0.0)
                bank_amount = min(temp_amount, bank_available)
                
                
                amount -= temp_amount
        
        else:
            
            nonbypass_available = 9.0 - data[2]
            amount = min(amount, nonbypass_available)
        
        
        amount = max(amount, 0.0)
        bank_amount = max(bank_amount, 0.0)
        
        audit(og_amount, amount, data[0], data[0]+amount, frozen=frozen, bypass=bypass, ldsv=reason)
        
        
        if not frozen or bypass:
            _m1_script0x2daffection__is_dirty = True
            data[0] += amount
            data[1] += bank_amount
            
            if not bypass:
                data[2] += amount
            
            else:
                data[3] += amount
            
            _m1_script0x2daffection__set_pers_data(_m1_script0x2daffection__encode_data(*data))

    def _remove_aff(amount, reason=None):
        """
        Removes some affection

        IN:
            amount - float - amount of affection to remove
            reason - str/None - the reason for this lose,
                MUST be current topic label or None
                (Default: None)
        """
        global _m1_script0x2daffection__is_dirty
        
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError("Invalid value for affection: {}".format(amount))
        
        data = _m1_script0x2daffection__get_data()
        if not data:
            return
        
        og_amount = amount
        amount = max(0.01, random.gauss(amount, 0.25))
        
        max_lose = data[0] + 1000000
        amount = min(amount, max_lose)
        
        base_change = 0.0
        bank_change = 0.0
        split_multi = 0.4
        bank_lose_multi = 1.25
        
        if data[1] > 0.0:
            base_change = amount * split_multi
            bank_change = amount - base_change
            
            if data[1] < bank_change:
                bank_change = data[1]
                base_change = amount - bank_change
            
            else:
                bank_change = min(bank_change*bank_lose_multi, data[1])
        
        else:
            base_change = amount
            bank_change = 0.0
        
        
        base_change = max(base_change, 0.0)
        bank_change = max(bank_change, 0.0)
        
        audit(og_amount, base_change, data[0], data[0]-base_change, ldsv=reason)
        
        _m1_script0x2daffection__is_dirty = True
        data[0] -= base_change
        data[1] -= bank_change
        _m1_script0x2daffection__set_pers_data(_m1_script0x2daffection__encode_data(*data))

    def _withdraw_aff():
        """
        Withdraws some aff daily
        from the bank to the main pool
        """
        global _m1_script0x2daffection__is_dirty
        
        data = _m1_script0x2daffection__get_data()
        if not data or not data[1]:
            return
        
        now_ = time.time()
        data[5] = _m1_script0x2daffection__validate_timestamp(data[5], now_)
        
        withdraw_date = datetime.date.fromtimestamp(data[5])
        if not store.mas_pastOneDay(withdraw_date):
            return
        
        data[5] = now_
        
        og_change = change = max(min(data[1], 5.0), 0.0)
        
        
        max_change = max(1000000-data[0], 0.0)
        change = min(change, max_change)
        
        audit(og_change, change, data[0], data[0]+change, ldsv="[withdraw]")
        
        _m1_script0x2daffection__is_dirty = True
        data[0] += change
        data[1] -= change
        _m1_script0x2daffection__set_pers_data(_m1_script0x2daffection__encode_data(*data))

    def _absence_decay_aff():
        """
        Removes some aff during absence
        """
        global _m1_script0x2daffection__is_dirty
        
        data = _m1_script0x2daffection__get_data()
        if not data:
            return
        
        if not data[1]:
            return
        
        seconds = persistent._mas_absence_time.total_seconds()
        if seconds > 86400*3:
            if data[1] <= 1.0:
                change = data[1]
            
            else:
                rate = 0.1 if not persistent._mas_long_absence else 0.025
                
                change = data[1] * min(rate*seconds/86400, 1.0)
            
            change = max(change, 0.0)
            
            _m1_script0x2daffection__is_dirty = True
            data[1] -= change
            _m1_script0x2daffection__set_pers_data(_m1_script0x2daffection__encode_data(*data))

    def _reset_aff(reason="RESET"):
        """
        Resets aff value (and only it)
        This is a dangerous func, use with care
        """
        _m1_script0x2daffection__set_aff(0.0, reason)

    def _transfer_aff_2nd_gen():
        """
        Transfers aff from the first gen to the second gen
        This may be dangerous, use wisely, don't fook up
        """
        global _m1_script0x2daffection__is_dirty
        
        if persistent._mas_affection_version >= 2:
            return
        
        old_data = persistent._mas_affection
        if old_data is None:
            persistent._mas_affection_version += 1
            return
        
        new_data = list()
        
        aff = old_data.get("affection", 0.0)
        if aff >= 1000000:
            aff = 0.0
        new_data.append(aff)
        new_data.append(0.0)
        new_data.append(old_data.get("today_exp", 0.0))
        new_data.append(0.0)
        freeze_date = old_data.get("freeze_date", None)
        if freeze_date is None:
            freeze_ts = time.time()
        else:
            freeze_ts = time.mktime(freeze_date.timetuple())
        new_data.append(freeze_ts)
        new_data.append(time.time())
        new_data.append(7.0)
        
        new_data = _m1_script0x2daffection__encode_data(*new_data)
        
        _m1_script0x2daffection__is_dirty = True
        _m1_script0x2daffection__set_pers_data(new_data)
        
        persistent._mas_affection_should_apologise = old_data.get("apologyflag", False)
        
        persistent._mas_affection = collections.defaultdict(float)
        persistent._mas_affection_version += 1

    def _m1_script0x2daffection__set_aff(amount, reason="SET"):
        """
        Sets affection to a value

        NOTE: never use this to add / lower affection unless its to
            strictly set affection to a level for some reason.

        IN:
            amount - amount to set affection to
            logmsg - msg to show in the log
                (Default: 'SET')
        """
        global _m1_script0x2daffection__is_dirty
        
        curr_data = _m1_script0x2daffection__get_data()
        if not curr_data:
            return
        
        amount = float(amount)
        og_amount = amount
        amount = max(min(amount, 1000000), -1000000)
        
        audit(abs(og_amount-curr_data[0]), abs(amount-curr_data[0]), curr_data[0], amount, ldsv=reason)
        
        _m1_script0x2daffection__is_dirty = True
        curr_data[0] = amount
        _m1_script0x2daffection__set_pers_data(_m1_script0x2daffection__encode_data(*curr_data))

    def _set_aff(value, reason):
        if store.config.developer:
            _m1_script0x2daffection__set_aff(value, reason)

    def save_aff():
        """
        Runs saving logic
        """
        
        
        
        
        
        
        persistent._mas_pctaieibe = None
        persistent._mas_pctaneibe = None
        persistent._mas_pctadeibe = None
        
        
        log.info("SAVE | {0}".format(_get_aff()))
        
        
        if _has_mismatch():
            _make_backup(True)

    def load_aff():
        """
        Runs loading logic
        """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        persistent._mas_pctaieibe = None
        persistent._mas_pctaneibe = None
        persistent._mas_pctadeibe = None
        
        data = _m1_script0x2daffection__get_data()
        aff = 0.0
        
        if data is None:
            
            success = _restore_backup()
            if success:
                txt_audit("LOAD", "Loading from backup")
                _make_backup()
            
            else:
                
                _m1_script0x2daffection__reset_pers_data()
                txt_audit("LOAD", "DATA HAS BEEN RESET")
            
            aff = _get_aff()
        
        else:
            
            aff = data[0]
            txt_audit("LOAD", "Loading from system")
            
            raw_audit(0.0, aff, aff, "LOAD?")
            
            if _has_mismatch():
                
                persistent._mas_aff_mismatches += 1
                txt_audit("MISMATCHES", persistent._mas_aff_mismatches)
                _restore_backup()
                aff = _get_aff()
            
            
            _make_backup()
        
        txt_audit("LOAD COMPLETE", aff)

    def _make_backup(force=False):
        """
        Runs backup algo for affection

        IN:
            force - boolean - should we force this?
        """
        backups = persistent._mas_affection_backups
        today = datetime.date.today()
        
        if force or not backups or backups[-1][0] < today:
            curr_raw_data = _m1_script0x2daffection__get_pers_data()
            curr_data = _m1_script0x2daffection__decode_data(curr_raw_data)
            
            if curr_data is not None:
                curr_value = curr_data[0]
                if backups:
                    backup_value = _m1_script0x2daffection__decode_data(backups[-1][-1])[0]
                
                else:
                    backup_value = None
                
                log.info("SET BACKUP | {0} -> {1}".format(backup_value, curr_value))
                backup = (today, curr_raw_data)
                backups.append(backup)
            
            else:
                log.info("FAILED TO BACKUP, CURRENT DATA IS BAD")

    def _has_mismatch():
        """
        Checks if the last backup mismatches with the current aff
        """
        backups = persistent._mas_affection_backups
        if not backups:
            return False
        
        return backups[-1][1] != _m1_script0x2daffection__get_pers_data()

    def _remove_backups():
        """
        Removes all backups
        """
        backups = persistent._mas_affection_backups
        if backups:
            backups.clear()

    def _restore_backup():
        """
        Uses available aff backup
        Use wisely

        OUT:
            boolean - whether or not a backup was restored
        """
        global _m1_script0x2daffection__is_dirty
        
        backups = persistent._mas_affection_backups
        if not backups:
            log.info("NO BACKUPS FOUND")
            return False
        
        while backups:
            backup = backups.pop()
            backup_data = _m1_script0x2daffection__decode_data(backup[1])
            
            if backup_data is None:
                log.info("FOUND CORRUPTED BACKUP")
                continue
            
            log.info("RESTORED | {}".format(backup_data[0]))
            _m1_script0x2daffection__is_dirty = True
            _m1_script0x2daffection__set_pers_data(backup[1])
            return True
        
        log.info("NO WORKING BACKUPS FOUND")
        return False




    AFF_MAX_POS_TRESH = 100
    AFF_MIN_POS_TRESH = 30
    AFF_MIN_NEG_TRESH = -30
    AFF_MAX_NEG_TRESH = -75


    AFF_BROKEN_MIN = -100
    AFF_DISTRESSED_MIN = -75
    AFF_UPSET_MIN = -30
    AFF_HAPPY_MIN = 50
    AFF_AFFECTIONATE_MIN = 100
    AFF_ENAMORED_MIN = 400
    AFF_LOVE_MIN = 1000


    AFF_MOOD_HAPPY_MIN = 30
    AFF_MOOD_SAD_MIN = -30


    AFF_TIME_CAP = -101


init -500 python in mas_affection:
    import os
    import datetime
    import store.mas_utils as mas_utils
    import store




















    log = store.mas_logging.init_log(
        "aff_log",
        formatter=store.mas_logging.logging.Formatter(
            fmt="[%(asctime)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        ),
        rotations=50
    )



    _AUDIT_FMT = "{0} | {1} -> {2} | {3} -> {4}"


    _AUDIT_FREEZE_FMT = "{5} | {0} | {1} -> {2} | {3} -> {4}"
    _FREEZE_TEXT = "!FREEZE!"
    _BYPASS_TEXT = "!BYPASS!"

    _RAW_AUDIT_FMT = "{0} | {1} | {2} -> {3}"

    def audit(
        attempted_change,
        change,
        old,
        new,
        frozen=False,
        bypass=False,
        ldsv=None
    ):
        """
        Audits a change in affection.

        IN:
            attempted_change - the attempted aff change
            change - the amount we are changing by
            old -the old value of affection
            new - what the new affection value will be
            frozen - True means we were frozen, false measn we are not
            bypass - True means we bypassed, false means we did not
            ldsv - Set to the string to use instead of monikatopic
                NOTE: for load / save operations ONLY
        """
        if ldsv is None:
            piece_one = store.persistent.current_monikatopic
        else:
            piece_one = ldsv
        
        if frozen:
            
            
            if bypass:
                piece_six = _BYPASS_TEXT
            else:
                piece_six = _FREEZE_TEXT
            
            
            audit_text = _AUDIT_FREEZE_FMT.format(
                piece_one,
                attempted_change,
                change,
                old,
                new,
                piece_six
            )
        
        else:
            audit_text = _AUDIT_FMT.format(
                piece_one,
                attempted_change,
                change,
                old,
                new
            )
        
        log.info(audit_text)

    def raw_audit(old, new, change, tag):
        """
        Non affection-dependent auditing for general usage.

        IN:
            old - the "old" value
            new - the "new" value
            change - the chnage amount
            tag - a string to label this audit change
        """
        log.info(_RAW_AUDIT_FMT.format(
            tag,
            change,
            old,
            new
        ))

    def txt_audit(tag, msg):
        """
        Generic auditing in the aff log

        IN:
            tag - a string to label thsi audit
            msg - message to show
        """
        log.info("{0} | {1}".format(
            tag,
            msg
        ))

    @mas_utils.deprecated()
    def _force_exp():
        """
        Determines appropriate forced expression for current affection.
        """
        curr_aff = store.mas_curr_affection
        
        if store.mas_isMoniNormal() and store.mas_isBelowZero():
            
            return "monika 1esc_static"
        
        return FORCE_EXP_MAP.get(curr_aff, "monika idle")


init 5 python in mas_affection:

    RANDCHAT_RANGE_MAP = {
        BROKEN: store.mas_randchat.RARELY,
        DISTRESSED: store.mas_randchat.OCCASIONALLY,
        UPSET: store.mas_randchat.LESS_OFTEN,
        NORMAL: store.mas_randchat.NORMAL,
        HAPPY: store.mas_randchat.NORMAL,
        AFFECTIONATE: store.mas_randchat.OFTEN,
        ENAMORED: store.mas_randchat.VERY_OFTEN,
        LOVE: store.mas_randchat.VERY_OFTEN
    }



init 15 python in mas_affection:
    import store 
    import store.evhand as evhand
    import store.mas_selspr as mas_selspr
    import store.mas_layout as mas_layout
    persistent = renpy.game.persistent
    layout = store.layout













    def _brokenToDis():
        """
        Runs when transitioning from broken to distressed
        """
        
        layout.QUIT_YES = mas_layout.QUIT_YES_DIS
        layout.QUIT_NO = mas_layout.QUIT_NO_UPSET
        layout.QUIT = mas_layout.QUIT
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_moni_idle_disp.update()


    def _disToBroken():
        """
        Runs when transitioning from distressed to broken
        """
        
        layout.QUIT_YES = mas_layout.QUIT_YES_BROKEN
        layout.QUIT_NO = mas_layout.QUIT_NO_BROKEN
        layout.QUIT = mas_layout.QUIT_BROKEN
        
        
        store.mas_randchat.reduceRandchatForAff(BROKEN)
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_moni_idle_disp.update()


    def _disToUpset():
        """
        Runs when transitioning from distressed to upset
        """
        
        layout.QUIT_YES = mas_layout.QUIT_YES
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_moni_idle_disp.update()


    def _upsetToDis():
        """
        Runs when transitioning from upset to distressed
        """
        
        layout.QUIT_YES = mas_layout.QUIT_YES_DIS
        if persistent._mas_acs_enable_promisering:
            renpy.store.monika_chr.remove_acs(renpy.store.mas_acs_promisering)
            persistent._mas_acs_enable_promisering = False
        
        
        store.mas_randchat.reduceRandchatForAff(DISTRESSED)
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        if store.monika_chr.clothes != store.mas_clothes_def:
            store.MASEventList.push("mas_change_to_def",skipeval=True)
        
        
        store.mas_moni_idle_disp.update()


    def _upsetToNormal():
        """
        Runs when transitioning from upset to normal
        """
        
        layout.QUIT_NO = mas_layout.QUIT_NO
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_songs.checkSongAnalysisDelegate()
        
        
        store.mas_moni_idle_disp.update()


    def _normalToUpset():
        """
        Runs when transitioning from normal to upset
        """
        
        layout.QUIT_NO = mas_layout.QUIT_NO_UPSET
        
        
        store.mas_randchat.reduceRandchatForAff(UPSET)
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_moni_idle_disp.update()


    def _normalToHappy():
        """
        Runs when transitioning from noraml to happy
        """
        
        layout.QUIT_NO = mas_layout.QUIT_NO_HAPPY
        
        
        if persistent._mas_text_speed_enabled:
            store.mas_enableTextSpeed()
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        if not store.seen_event("mas_blazerless_intro") and not store.mas_hasSpecialOutfit():
            store.MASEventList.queue("mas_blazerless_intro")
        
        
        store.mas_selspr.unlock_clothes(store.mas_clothes_blazerless)
        
        
        store.mas_rmallEVL("mas_change_to_def")
        
        
        store.mas_songs.checkSongAnalysisDelegate(HAPPY)
        
        
        store.mas_moni_idle_disp.update()


    def _happyToNormal():
        """
        Runs when transitinong from happy to normal
        """
        
        layout.QUIT_NO = mas_layout.QUIT_NO
        
        
        store.mas_disableTextSpeed()
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        if store.monika_chr.clothes != store.mas_clothes_def and not store.mas_hasSpecialOutfit():
            store.MASEventList.push("mas_change_to_def",skipeval=True)
        
        
        store.mas_songs.checkSongAnalysisDelegate(NORMAL)
        
        
        store.mas_moni_idle_disp.update()


    def _happyToAff():
        """
        Runs when transitioning from happy to affectionate
        """
        
        layout.QUIT_YES = mas_layout.QUIT_YES_AFF
        if persistent.gender == "M" or persistent.gender == "F":
            layout.QUIT_NO = mas_layout.QUIT_NO_AFF_G
        else:
            layout.QUIT_NO = mas_layout.QUIT_NO_AFF_GL
        layout.QUIT = mas_layout.QUIT_AFF
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_songs.checkSongAnalysisDelegate(AFFECTIONATE)
        
        
        store.mas_moni_idle_disp.update()

    def _affToHappy():
        """
        Runs when transitioning from affectionate to happy
        """
        
        layout.QUIT_YES = mas_layout.QUIT_YES
        layout.QUIT_NO = mas_layout.QUIT_NO_HAPPY
        layout.QUIT = mas_layout.QUIT
        
        
        
        
        
        
        
        
        persistent._mas_monika_nickname = "Monika"
        store.m_name = persistent._mas_monika_nickname
        
        
        store.mas_randchat.reduceRandchatForAff(HAPPY)
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_songs.checkSongAnalysisDelegate(HAPPY)
        
        
        store.mas_moni_idle_disp.update()

    def _affToEnamored():
        """
        Runs when transitioning from affectionate to enamored
        """
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_songs.checkSongAnalysisDelegate(ENAMORED)
        
        
        store.mas_moni_idle_disp.update()

    def _enamoredToAff():
        """
        Runs when transitioning from enamored to affectionate
        """
        
        store.mas_randchat.reduceRandchatForAff(AFFECTIONATE)
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_songs.checkSongAnalysisDelegate(AFFECTIONATE)
        
        
        store.mas_moni_idle_disp.update()

    def _enamoredToLove():
        """
        Runs when transitioning from enamored to love
        """
        
        layout.QUIT_NO = mas_layout.QUIT_NO_LOVE
        
        
        store.mas_unlockEventLabel("mas_compliment_thanks", eventdb=store.mas_compliments.compliment_database)
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_songs.checkSongAnalysisDelegate(LOVE)
        
        
        store.mas_moni_idle_disp.update()

    def _loveToEnamored():
        """
        Runs when transitioning from love to enamored
        """
        
        if store.seen_event("mas_compliment_thanks"):
            store.mas_lockEventLabel("mas_compliment_thanks", eventdb=store.mas_compliments.compliment_database)
        
        
        store.mas_idle_mailbox.send_rebuild_msg()
        
        
        store.mas_songs.checkSongAnalysisDelegate(ENAMORED)
        
        
        store.mas_moni_idle_disp.update()

    def _gSadToNormal():
        """
        Runs when transitioning from sad group to normal group
        """
        return


    def _gNormalToSad():
        """
        Runs when transitioning from normal group to sad group
        """
        return


    def _gNormalToHappy():
        """
        Runs when transitioning from normal group to happy group
        """
        return


    def _gHappyToNormal():
        """
        Runs when transitioning from happy group to normal group
        """
        return










    _trans_pps = {
        BROKEN: (_brokenToDis, None),
        DISTRESSED: (_disToUpset, _disToBroken),
        UPSET: (_upsetToNormal, _upsetToDis),
        NORMAL: (_normalToHappy, _normalToUpset),
        HAPPY: (_happyToAff, _happyToNormal),
        AFFECTIONATE: (_affToEnamored, _affToHappy),
        ENAMORED: (_enamoredToLove, _enamoredToAff),
        LOVE: (None, _loveToEnamored)
    }


    _transg_pps = {
        G_SAD: (_gSadToNormal, None),
        G_NORMAL: (_gNormalToHappy, _gNormalToSad),
        G_HAPPY: (None, _gHappyToNormal)
    }


    def runAffPPs(start_aff, end_aff):
        """
        Runs programming points to transition from the starting affection
        to the ending affection

        IN:
            start_aff - starting affection
            end_aff - ending affection
        """
        comparison = _compareAff(start_aff, end_aff)
        if comparison == 0:
            
            return
        
        
        start_index = _aff_order.index(start_aff)
        end_index = _aff_order.index(end_aff)
        if comparison < 0:
            for index in range(start_index, end_index):
                to_up, to_down = _trans_pps[_aff_order[index]]
                if to_up is not None:
                    to_up()
        
        else:
            for index in range(start_index, end_index, -1):
                to_up, to_down = _trans_pps[_aff_order[index]]
                if to_down is not None:
                    to_down()
        
        
        store.mas_rebuildEventLists()


    def runAffGPPs(start_affg, end_affg):
        """
        Runs programming points to transition from the starting affection group
        to the ending affection group

        IN:
            start_affg - starting affection group
            end_affg - ending affection group
        """
        comparison = _compareAffG(start_affg, end_affg)
        if comparison == 0:
            
            return
        
        
        start_index = _affg_order.index(start_affg)
        end_index = _affg_order.index(end_affg)
        if comparison < 0:
            for index in range(start_index, end_index):
                to_up, to_down = _transg_pps[_affg_order[index]]
                if to_up is not None:
                    to_up()
        
        else:
            for index in range(start_index, end_index, -1):
                to_up, to_down = _transg_pps[_affg_order[index]]
                if to_down is not None:
                    to_down()


    def _isMoniState(aff_1, aff_2, lower=False, higher=False):
        """
        Compares the given affection values according to the affection
        state system

        By default, this will check if aff_1 == aff_2

        IN:
            aff_1 - affection to compare
            aff_2 - affection to compare
            lower - True means we want to check aff_1 <= aff_2
            higher - True means we want to check aff_1 >= aff_2

        RETURNS:
            True if the given affections pass the test we want to do.
            False otherwise
        """
        comparison = _compareAff(aff_1, aff_2)
        
        if comparison == 0:
            return True
        
        if lower:
            return comparison <= 0
        
        if higher:
            return comparison >= 0
        
        return False


    def _isMoniStateG(affg_1, affg_2, lower=False, higher=False):
        """
        Compares the given affection groups according to the affection group
        system

        By default, this will check if affg_1 == affg_2

        IN:
            affg_1 - affection group to compare
            affg_2 - affection group to compare
            lower - True means we want to check affg_1 <= affg_2
            higher - True means we want to check affg_1 >= affg_2

        RETURNS:
            true if the given affections pass the test we want to do.
            False otherwise
        """
        comparison = _compareAffG(affg_1, affg_2)
        
        if comparison == 0:
            return True
        
        if lower:
            return comparison <= 0
        
        if higher:
            return comparison >= 0
        
        return False








    talk_menu_quips = dict()
    play_menu_quips = dict()

    def _init_talk_quips():
        """
        Initializes the talk quiplists
        """
        global talk_menu_quips
        def save_quips(_aff, quiplist):
            mas_ql = store.MASQuipList(allow_label=False)
            for _quip in quiplist:
                mas_ql.addLineQuip(_quip)
            talk_menu_quips[_aff] = mas_ql
        
        
        
        quips = [
            "..."
        ]
        save_quips(BROKEN, quips)
        
        
        quips = [
            _("..."),
            _("Yes?"),
            _("Oh..."),
            _("Huh..."),
            _("I guess we can talk."),
            _("You want to talk?"),
            _("...Go ahead."),
            _("Are you sure you want to talk to me?"),
            _("You actually want to talk to me?"),
            _("Alright...{w=0.3}if that's what you want."),
            _("Is this really what you want?"),
        ]
        save_quips(DISTRESSED, quips)
        
        
        quips = [
            _("..."),
            _("What?"),
            _("Huh?"),
            _("Yeah?"),
            _("What do you want?"),
            _("What now?"),
            _("What is it?"),
            _("Go on then."),
            _("I hope this is important."),
            _("Something on your mind?"),
            _("Yes, [player]?"),
        ]
        save_quips(UPSET, quips)
        
        
        quips = [
            _("What would you like to talk about?"),
            _("What are you thinking of?"),
            _("Is there something you'd like to talk about?"),
            _("Something on your mind?"),
            _("Yes, [player]?"),
        ]
        save_quips(NORMAL, quips)
        
        
        quips = [
            _("What would you like to talk about?"),
            _("What are you thinking of?"),
            _("Is there something you'd like to talk about?"),
            _("Something on your mind?"),
            _("Up to chat, [player]?"),
            _("Yes, [player]?"),
            _("What's on your mind, [player]?"),
            _("What's up, [player]?"),
            _("Ask away, [player]."),
            _("Don't be shy, [player]."),
        ]
        save_quips(HAPPY, quips)
        
        
        quips = [
            _("What would you like to talk about?"),
            _("What would you like to talk about, [mas_get_player_nickname()]?"),
            _("What are you thinking of?"),
            _("Is there something you'd like to talk about, [mas_get_player_nickname()]?"),
            _("Something on your mind?"),
            _("Something on your mind, [mas_get_player_nickname()]?"),
            _("Up to chat, [mas_get_player_nickname()]?"),
            _("Yes, [mas_get_player_nickname()]?"),
            _("What's on your mind, [mas_get_player_nickname()]?"),
            _("What's up, [mas_get_player_nickname()]?"),
            _("Ask away, [mas_get_player_nickname()]."),
            _("Don't be shy, [mas_get_player_nickname()]~"),
            _("I'm all ears, [mas_get_player_nickname()]~"),
            _("Of course we can talk, [mas_get_player_nickname()]."),
        ]
        save_quips(AFFECTIONATE, quips)
        
        
        quips = [
            _("What would you like to talk about? <3"),
            _("What would you like to talk about, [mas_get_player_nickname()]? <3"),
            _("What are you thinking of?"),
            _("Is there something you'd like to talk about, [mas_get_player_nickname()]?"),
            _("Something on your mind?"),
            _("Something on your mind, [mas_get_player_nickname()]?"),
            _("Up to chat, I see~"),
            _("Yes, [mas_get_player_nickname()]?"),
            _("What's on your mind, [mas_get_player_nickname()]?"),
            _("What's up, [player]?"),
            _("Ask away, [mas_get_player_nickname()]~"),
            _("I'm all ears, [mas_get_player_nickname()]~"),
            _("Of course we can talk, [mas_get_player_nickname()]~"),
            _("Take all the time you need, [player]."),
            _("We can talk about whatever you'd like, [mas_get_player_nickname()]."),
        ]
        save_quips(ENAMORED, quips)
        
        
        quips = [
            _("What would you like to talk about? <3"),
            _("What would you like to talk about, [mas_get_player_nickname()]? <3"),
            _("What are you thinking of?"),
            _("Something on your mind?"),
            _("Something on your mind, [mas_get_player_nickname()]?"),
            _("Up to chat, I see~"),
            _("Yes, [mas_get_player_nickname()]?"),
            _("What's on your mind, [mas_get_player_nickname()]?"),
            _("<3"),
            _("What's up, [mas_get_player_nickname()]?"),
            _("Ask away, [mas_get_player_nickname()]~"),
            _("I'm all ears, [mas_get_player_nickname()]~"),
            _("We can talk about whatever you'd like, [mas_get_player_nickname()]."),
            _("Of course we can talk, [mas_get_player_nickname()]~"),
            _("Take all the time you need, [mas_get_player_nickname()]~"),
            _("I'm all yours, [mas_get_player_nickname()]~"),
            _("Oh? Something...{w=0.3}{i}important{/i} on your mind, [mas_get_player_nickname()]?~"),
        ]
        save_quips(LOVE, quips)


    def _init_play_quips():
        """
        Initializes the play quipliust
        """
        global play_menu_quips
        def save_quips(_aff, quiplist):
            mas_ql = store.MASQuipList(allow_label=False)
            for _quip in quiplist:
                mas_ql.addLineQuip(_quip)
            play_menu_quips[_aff] = mas_ql
        
        
        
        quips = [
            _("...")
        ]
        save_quips(BROKEN, quips)
        
        
        quips = [
            _("..."),
            _("If that's what you want..."),
            _("I suppose it wouldn't hurt to give this a try..."),
            _("...Really?"),
        ]
        save_quips(DISTRESSED, quips)
        
        
        quips = [
            _("..."),
            _("If that's what you want..."),
            _("...Really?"),
            _("Oh, okay..."),
        ]
        save_quips(UPSET, quips)
        
        
        quips = [
            _("What would you like to play?"),
            _("Is there something you had in mind?"),
            _("Anything specific you'd like to play?"),
            _("What should we play today, [player]?"),
            _("Sure, I'm up for a game."),
        ]
        save_quips(NORMAL, quips)
        
        
        quips = [
            _("What would you like to play?"),
            _("Is there something you had in mind?"),
            _("Anything specific you'd like to play?"),
            _("What should we play today, [player]?"),
            _("Sure, I'm up for a game!"),
        ]
        save_quips(HAPPY, quips)
        
        
        quips = [
            _("What would you like to play?"),
            _("Choose anything you like, [mas_get_player_nickname()]."),
            _("What should we play today, [mas_get_player_nickname()]?"),
            _("Sure, I'm up for a game!"),
            _("Pick anything you like."),
        ]
        save_quips(AFFECTIONATE, quips)
        
        
        quips = [
            _("What would you like to play? <3"),
            _("Pick a game, any game~"),
            _("Choose anything you like, [mas_get_player_nickname()]."),
            _("Pick anything you like, [mas_get_player_nickname()]."),
        ]
        save_quips(ENAMORED, quips)
        
        
        quips = [
            _("What would you like to play? <3"),
            _("Choose anything you like, [mas_get_player_nickname()]."),
            _("Pick anything you like, [mas_get_player_nickname()]."),
            _("Pick a game, any game~"),
            _("I'd love to play something with you, [mas_get_player_nickname()]~"),
            _("Sure, I'd love to play with you!"),
            _("I'll always be up to play with you, [mas_get_player_nickname()]~"),
        ]
        save_quips(LOVE, quips)

    _init_talk_quips()
    _init_play_quips()


    def _dict_quip(_quips):
        """
        Returns a quip based on the current affection using the given quip
        dict

        IN:
            _quips - quip dict to pull from

        RETURNS:
            quip or empty string if failure
        """
        quipper = _quips.get(store.mas_curr_affection, None)
        if quipper is not None:
            return quipper.quip()
        
        return ""


    def talk_quip():
        """
        Returns a talk quip based on the current affection
        """
        quip = _dict_quip(talk_menu_quips)
        if len(quip) > 0:
            return quip
        return _("What would you like to talk about?")


    def play_quip():
        """
        Returns a play quip based on the current affection
        """
        quip = _dict_quip(play_menu_quips)
        if len(quip) > 0:
            return quip
        return _("What would you like to play?")


default persistent._mas_long_absence = False
default persistent._mas_pctaieibe = None
default persistent._mas_pctaneibe = None
default persistent._mas_pctadeibe = None
default persistent._mas_aff_backup = None
default persistent._mas_aff_mismatches = 0

init -10 python:
    if persistent._mas_aff_mismatches is None:
        persistent._mas_aff_mismatches = 0

    def _mas_AffSave():
        """
        Runs saving algo for affection
        """
        mas_affection.save_aff()

    def _mas_AffLoad():
        """
        Runs loading algo for affection
        """
        mas_affection.load_aff()


init python:

    import datetime
    import store.mas_affection as affection
    import store.mas_utils as mas_utils

    @mas_utils.deprecated()
    def mas_FreezeGoodAffExp():
        pass

    @mas_utils.deprecated()
    def mas_FreezeBadAffExp():
        pass

    @mas_utils.deprecated()
    def mas_FreezeBothAffExp():
        pass

    @mas_utils.deprecated()
    def mas_UnfreezeBadAffExp():
        pass

    @mas_utils.deprecated()
    def mas_UnfreezeGoodAffExp():
        pass

    @mas_utils.deprecated()
    def mas_UnfreezeBothExp():
        pass

    def _mas_getAffection():
        """
        Tries to return current affection

        OUT:
            float
        """
        return mas_affection._get_aff()

    @mas_utils.deprecated(use_instead="_get_current_aff_lose")
    def _mas_getBadExp():
        return _get_current_aff_lose()

    @mas_utils.deprecated(use_instead="_get_current_aff_gain")
    def _mas_getGoodExp():
        return _get_current_aff_gain()

    @mas_utils.deprecated()
    def _mas_getTodayExp():
        return 0.0

    def mas_isBelowZero():
        """
        Checks if affection is negative

        OUT:
            boolean
        """
        return _mas_getAffection() < 0.0



    def mas_betweenAff(aff_low, aff_check, aff_high):
        """
        Checks if the given affection is between the given affection levels.

        If low is actually greater than high, then False is always returned

        IN:
            aff_low - the lower bound of affecton to check with (inclusive)
                if None, then we assume no lower bound
            aff_check - the affection to check
            aff_high - the upper bound of affection to check with (inclusive)
                If None, then we assume no upper bound

        RETURNS:
            True if the given aff check is within the bounds of the given
            lower and upper affection limits, False otherwise.
            If low is greater than high, False is returned.
        """
        return mas_affection._betweenAff(aff_low, aff_check, aff_high)


    def mas_compareAff(aff_1, aff_2):
        """
        Runs compareTo logic on the given affection states

        IN:
            aff_1 - an affection state to compare
            aff_2 - an affection state to compare

        RETURNS:
            negative number if aff_1 < aff_2
            0 if aff_1 == aff_2
            postitive number if aff_1 > aff_2
            Returns 0 if a non affection state was provided
        """
        return mas_affection._compareAff(aff_1, aff_2)


    def mas_compareAffG(affg_1, affg_2):
        """
        Runs compareTo logic on the given affection groups

        IN:
            affg_1 - an affection group to compare
            affg_2 - an affection group to compare

        RETURNS:
            negative number if affg_1 < affg_2
            0 if affg_1 == affg_2
            positive numbre if affg_1 > affg_2
            Returns 0 if a non affection group was provided
        """
        return mas_affection._compareAffG(affg_1, affg_2)




    def mas_isMoniBroken(lower=False, higher=False):
        """
        Checks if monika is broken

        IN:
            lower - True means we include everything below this affection state
                as broken as well
                (Default: False)
            higher - True means we include everything above this affection
                state as broken as well
                (Default: False)

        RETURNS:
            True if monika is broke, False otherwise
        """
        return mas_affection._isMoniState(
            mas_curr_affection,
            store.mas_affection.BROKEN,
            higher=higher
        )


    def mas_isMoniDis(lower=False, higher=False):
        """
        Checks if monika is distressed

        IN:
            lower - True means we cinlude everything below this affection state
                as distressed as well
                NOTE: takes precedence over higher
                (Default: False)
            higher - True means we include everything above this affection
                state as distressed as well
                (Default: FAlse)

        RETURNS:
            True if monika is distressed, false otherwise
        """
        return mas_affection._isMoniState(
            mas_curr_affection,
            store.mas_affection.DISTRESSED,
            lower=lower,
            higher=higher
        )


    def mas_isMoniUpset(lower=False, higher=False):
        """
        Checks if monika is upset

        IN:
            lower - True means we include everything below this affection
                state as upset as well
                (Default: False)
            higher - True means we include everything above this affection
                state as upset as well
                (Default: False)

        RETURNS:
            True if monika is upset, false otherwise
        """
        return mas_affection._isMoniState(
            mas_curr_affection,
            store.mas_affection.UPSET,
            lower=lower,
            higher=higher
        )


    def mas_isMoniNormal(lower=False, higher=False):
        """
        Checks if monika is normal

        IN:
            lower - True means we include everything below this affection state
                as normal as well
                (Default: False)
            higher - True means we include evreything above this affection
                state as normal as well
                (Default: False)

        RETURNS:
            True if monika is normal, false otherwise
        """
        return mas_affection._isMoniState(
            mas_curr_affection,
            store.mas_affection.NORMAL,
            lower=lower,
            higher=higher
        )


    def mas_isMoniHappy(lower=False, higher=False):
        """
        Checks if monika is happy

        IN:
            lower - True means we include everything below this affection
                state as happy as well
                (Default: False)
            higher - True means we include everything above this affection
                state as happy as well
                (Default: False)

        RETURNS:
            True if monika is happy, false otherwise
        """
        return mas_affection._isMoniState(
            mas_curr_affection,
            store.mas_affection.HAPPY,
            lower=lower,
            higher=higher
        )


    def mas_isMoniAff(lower=False, higher=False):
        """
        Checks if monika is affectionate

        IN:
            lower - True means we include everything below this affection
                state as affectionate as well
                (Default: FAlse)
            higher - True means we include everything above this affection
                state as affectionate as well
                (Default: False)

        RETURNS:
            True if monika is affectionate, false otherwise
        """
        return mas_affection._isMoniState(
            mas_curr_affection,
            store.mas_affection.AFFECTIONATE,
            lower=lower,
            higher=higher
        )


    def mas_isMoniEnamored(lower=False, higher=False):
        """
        Checks if monika is enamored

        IN:
            lower - True means we include everything below this affection
                state as enamored as well
                (Default: False)
            higher - True means we include everything above this affection
                state as enamored as well
                (Default: False)

        RETURNS:
            True if monika is enamored, false otherwise
        """
        return mas_affection._isMoniState(
            mas_curr_affection,
            store.mas_affection.ENAMORED,
            lower=lower,
            higher=higher
        )


    def mas_isMoniLove(lower=False, higher=False):
        """
        Checks if monika is in love

        IN:
            lower - True means we include everything below this affectionate
                state as love as well
                (Default: False)
            higher - True means we include everything above this affection
                state as love as well
                (Default: False)

        RETURNS:
            True if monika in love, false otherwise
        """
        return mas_affection._isMoniState(
            mas_curr_affection,
            store.mas_affection.LOVE,
            lower=lower
        )



    def mas_isMoniGSad(lower=False, higher=False):
        """
        Checks if monika is in sad affection group

        IN:
            lower - True means we include everything below this affection
                group as sad as well
                (Default: False)
            higher - True means we include everything above this affection
                group as sad as well
                (Default: False)

        RETURNS:
            True if monika in sad group, false otherwise
        """
        return mas_affection._isMoniStateG(
            mas_curr_affection_group,
            store.mas_affection.G_SAD,
            higher=higher
        )


    def mas_isMoniGNormal(lower=False, higher=False):
        """
        Checks if monika is in normal affection group

        IN:
            lower - True means we include everything below this affection
                group as normal as well
                (Default: False)
            higher - True means we include everything above this affection
                group as normal as well
                (Default: False)

        RETURNS:
            True if monika is in normal group, false otherwise
        """
        return mas_affection._isMoniStateG(
            mas_curr_affection_group,
            store.mas_affection.G_NORMAL,
            lower=lower,
            higher=higher
        )


    def mas_isMoniGHappy(lower=False, higher=False):
        """
        Checks if monika is in happy affection group

        IN:
            lower - True means we include everything below this affection
                group as happy as well
                (Default: False)
            higher - True means we include everything above this affection
                group as happy as well
                (Default: FAlse)

        RETURNS:
            True if monika is in happy group, false otherwise
        """
        return mas_affection._isMoniStateG(
            mas_curr_affection_group,
            store.mas_affection.G_HAPPY,
            lower=lower
        )



    def mas_updateAffectionExp(skipPP=False):
        global mas_curr_affection
        global mas_curr_affection_group
        
        
        curr_affection = _mas_getAffection()
        
        
        new_aff = mas_curr_affection
        if curr_affection <= mas_affection.AFF_BROKEN_MIN:
            new_aff = mas_affection.BROKEN
        
        elif mas_affection.AFF_BROKEN_MIN < curr_affection <= mas_affection.AFF_DISTRESSED_MIN:
            new_aff = mas_affection.DISTRESSED
        
        elif mas_affection.AFF_DISTRESSED_MIN < curr_affection <= mas_affection.AFF_UPSET_MIN:
            new_aff = mas_affection.UPSET
        
        elif mas_affection.AFF_UPSET_MIN < curr_affection < mas_affection.AFF_HAPPY_MIN:
            new_aff = mas_affection.NORMAL
        
        elif mas_affection.AFF_HAPPY_MIN <= curr_affection < mas_affection.AFF_AFFECTIONATE_MIN:
            new_aff = store.mas_affection.HAPPY
        
        elif mas_affection.AFF_AFFECTIONATE_MIN <= curr_affection < mas_affection.AFF_ENAMORED_MIN:
            new_aff = mas_affection.AFFECTIONATE
        
        elif mas_affection.AFF_ENAMORED_MIN <= curr_affection < mas_affection.AFF_LOVE_MIN:
            new_aff = mas_affection.ENAMORED
        
        elif curr_affection >= mas_affection.AFF_LOVE_MIN:
            new_aff = mas_affection.LOVE
        
        
        if new_aff != mas_curr_affection:
            if not skipPP:
                mas_affection.runAffPPs(mas_curr_affection, new_aff)
            mas_curr_affection = new_aff
        
        
        new_affg = mas_curr_affection_group
        if curr_affection <= mas_affection.AFF_MOOD_SAD_MIN:
            new_affg = mas_affection.G_SAD
        
        elif curr_affection >= mas_affection.AFF_MOOD_HAPPY_MIN:
            new_affg = mas_affection.G_HAPPY
        
        else:
            new_affg = mas_affection.G_NORMAL
        
        if new_affg != mas_curr_affection_group:
            if not skipPP:
                mas_affection.runAffGPPs(mas_curr_affection_group, new_affg)
            mas_curr_affection_group = new_affg

    def _get_current_aff_gain():
        return mas_affection._m1_script0x2daffection__DEF_AFF_GAIN_MAP.get(
            mas_curr_affection,
            1.0
        )

    def _get_current_aff_lose():
        return mas_affection._m1_script0x2daffection__DEF_AFF_LOSE_MAP.get(
            mas_curr_affection,
            5.0
        )

    def _get_current_aff_fraction_lose():
        return mas_affection._m1_script0x2daffection__DEF_AFF_FRACTION_LOSE_MAP.get(
            mas_curr_affection,
            0.1
        )

    def mas_gainAffection(
        amount=None,
        modifier=1.0,
        bypass=False,
        current_evlabel=None
    ):
        """
        Grants some affection whenever something positive happens

        IN:
            amount - float, None - amount of affection to grant,
                If None, uses the default value for the current aff
                (Default: None)
            modifier - float - modifier for the amount value
                (Default: 1.0)
            bypass - bool - whether or not we should bypass the cap,
                for example during special events
                (Default: False)
            current_evlabel - str/None - the topic that caused this aff gain,
                MUST be current topic label or None.
                You probably DO NOT want to use this
                (Default: None)
        """
        if amount is None:
            amount = _get_current_aff_gain()
        change = amount*modifier
        
        if change <= 0.0:
            store.mas_utils.mas_log.error(
                "mas_gainAffection was called with invalid amount of affection: {}".format(change)
            )
            return
        
        mas_affection._grant_aff(change, bypass, reason=current_evlabel)
        
        mas_updateAffectionExp()

    def mas_loseAffection(
        amount=None,
        modifier=1.0,
        reason=None,
        ev_label=None,
        apology_active_expiry=datetime.timedelta(hours=3),
        apology_overall_expiry=datetime.timedelta(weeks=1),
        current_evlabel=None
    ):
        """
        Subtracts some affection whenever something negative happens

        A reason can be specified and used for the apology dialogue
        if the default value is used Monika won't comment on the reason,
        and slightly will recover affection
        if None is passed she won't acknowledge that there was need for an apology.
        DEFAULTS reason to an Empty String mostly because when this one is called
        is intended to be used for something the player can apologize for, but it's
        not totally necessary.
        NEW BITS:
        prompt: the prompt shown in the menu for apologizing
        expirydatetime:
        generic: do we want this to be persistent? or not

        IN:
            amount - float, None - amount of affection to subtract,
                If None, uses the default value for the current aff
                (Default: None)
            modifier - float - modifier for the amount value
                (Default: 1.0)
            reason - int, None, - a constant for the reason for the apology
                See mas_setApologyReason
                (Default: None)
            ev_label - string, None - the label for the apology event
                See mas_setApologyReason
                (Default: None)
            apology_active_expiry - datetime.timedelta - the amount of session time
                for the apology to expire
                (Default: 3 hours)
            apology_overall_expiry - datetime.timedelta - the amount of overall time
                for the apology to expire
                (Default: 1 week)
            current_evlabel - str/None - the topic that caused this aff gain,
                MUST be current topic label or None.
                You probably DO NOT want to use this
                (Default: None)
        """
        if amount is None:
            amount = _get_current_aff_lose()
        change = amount*modifier
        
        if change <= 0.0:
            store.mas_utils.mas_log.error(
                "mas_loseAffection was called with invalid amount of affection: {}".format(change)
            )
            return
        
        
        mas_setApologyReason(
            reason=reason,
            ev_label=ev_label,
            apology_active_expiry=apology_active_expiry,
            apology_overall_expiry=apology_overall_expiry
        )
        
        mas_affection._remove_aff(change, reason=current_evlabel)
        
        mas_updateAffectionExp()

    def mas_loseAffectionFraction(
        fraction=None,
        min_amount=None,
        modifier=1.0,
        reason=None,
        ev_label=None,
        apology_active_expiry=datetime.timedelta(hours=3),
        apology_overall_expiry=datetime.timedelta(weeks=1),
        current_evlabel=None
    ):
        """
        See mas_loseAffection for more info
        Subtracts portion of affection whenever something negative happens
        USE VERY WISELY

        IN:
            fraction - float, None - portion of affection to subtracts,
                If None, uses the default value for the current aff
                (Default: None)
            min_amount - float, None - minimal amount of affection to substruct,
                allows to verify that you take at least this amount, but no more
                than the provided fraction
                If None, uses the default value for the current aff
                (Default: None)
            modifier - float - modifier for the amount value
                NOTE: the modifier is being applied AFTER min_amount
                (Default: 1.0)
        """
        if fraction is None:
            fraction = _get_current_aff_fraction_lose()
        if min_amount is None:
            min_amount = _get_current_aff_lose()
        
        if fraction <= 0.0 or min_amount <= 0.0 or modifier <= 0.0:
            store.mas_utils.mas_log.error(
                (
                    "mas_loseAffectionFraction was called with one or more parameters "
                    "being invalid: fraction: {} min_amount: {} modifier: {}"
                ).format(
                    fraction,
                    min_amount,
                    modifier
                )
            )
            return
        
        curr_aff = _mas_getAffection()
        change = (curr_aff + 100.0)*fraction
        
        if change < 0.0:
            
            
            change = abs(change)
        
        change = max(min_amount, change)
        
        mas_loseAffection(
            change,
            modifier=modifier,
            reason=reason,
            ev_label=None,
            apology_active_expiry=apology_active_expiry,
            apology_overall_expiry=apology_overall_expiry,
            current_evlabel=current_evlabel
        )

    def _mas_revertFreshStart():
        """
        Revert affection to before the fresh start
        """
        curr_aff = _mas_getAffection()
        prev_aff = persistent._mas_aff_before_fresh_start
        if prev_aff is None:
            return
        
        change = curr_aff - prev_aff
        if change <= 0.0:
            return
        
        mas_loseAffection(change)

    def _mas_shatterAffection():
        """
        Sets affection to the lowest value
        """
        curr_aff = _mas_getAffection()
        if curr_aff <= -101.0:
            return
        
        mas_loseAffection(curr_aff+101.0)

    def _mas_doFreshStart():
        """
        Resets affection
        """
        if (
            persistent._mas_aff_before_fresh_start is None
            or not persistent._mas_pm_got_a_fresh_start
        ):
            return
        mas_affection._reset_aff("FRESH START")

    @store.mas_utils.deprecated()
    def mas_setAffection(*args, **kwargs):
        pass

    def mas_setApologyReason(
        reason=None,
        ev_label=None,
        apology_active_expiry=datetime.timedelta(hours=3),
        apology_overall_expiry=datetime.timedelta(weeks=1)
        ):
        """
        Sets a reason for apologizing

        IN:
            reason - The reason for the apology (integer value corresponding to item in the apology_reason_db)
                (if left None, and an ev_label is present, we assume a non-generic apology)
            ev_label - The apology event we want to unlock
                (required)
            apology_active_expiry - The amount of session time after which, the apology that was added expires
                defaults to 3 hours active time
            apology_overall_expiry - The amount of overall time after which, the apology that was added expires
                defaults to 7 days
        """
        
        global mas_apology_reason
        
        if ev_label is None:
            if reason is None:
                mas_apology_reason = 0
            else:
                mas_apology_reason = reason
            return
        elif mas_getEV(ev_label) is None:
            store.mas_utils.mas_log.error(
                "ev_label does not exist: {0}".format(repr(ev_label))
            )
            return
        
        if ev_label not in persistent._mas_apology_time_db:
            
            store.mas_unlockEVL(ev_label, 'APL')
            
            
            current_total_playtime = persistent.sessions['total_playtime'] + mas_getSessionLength()
            
            
            persistent._mas_apology_time_db[ev_label] = (current_total_playtime + apology_active_expiry,datetime.date.today() + apology_overall_expiry)
            return


    def mas_checkAffection():
        
        curr_affection = _mas_getAffection()
        
        
        if curr_affection <= -15 and not seen_event("mas_affection_upsetwarn"):
            MASEventList.queue("mas_affection_upsetwarn", notify=True)
        
        
        
        elif 15 <= curr_affection and not seen_event("mas_affection_happynotif"):
            MASEventList.queue("mas_affection_happynotif", notify=True)
        
        
        elif curr_affection >= 100 and not seen_event("monika_affection_nickname"):
            MASEventList.queue("monika_affection_nickname", notify=True)
        
        
        elif curr_affection <= -50 and not seen_event("mas_affection_apology"):
            if not persistent._mas_disable_sorry:
                MASEventList.queue("mas_affection_apology", notify=True)







    mas_apology_reason = None

    def _m1_script0x2daffection__long_absence_check():
        
        mas_affection._absence_decay_aff()
        
        if persistent._mas_long_absence or persistent._mas_is_backup:
            return
        
        time_difference = persistent._mas_absence_time
        
        
        if (
            not config.developer
            and not store.mas_globals.returned_home_this_sesh
            and time_difference >= datetime.timedelta(weeks=1)
        ):
            curr_aff = _mas_getAffection()
            calc_loss = 0.5 * time_difference.days
            new_aff = curr_aff - calc_loss
            
            if new_aff < mas_affection.AFF_TIME_CAP and curr_aff > mas_affection.AFF_TIME_CAP:
                
                store.mas_affection.txt_audit("ABS", "capped loss")
                mas_loseAffection(abs(mas_affection.AFF_TIME_CAP - curr_aff))
                
                
                if time_difference >= datetime.timedelta(days=(365 * 10)):
                    store.mas_affection.txt_audit("ABS", "10 year diff")
                    mas_loseAffection(200)
            
            else:
                store.mas_affection.txt_audit("ABS", "she missed you")
                mas_loseAffection(calc_loss)

    def _mas_AffStartup():
        
        
        _mas_AffLoad()
        
        
        
        mas_updateAffectionExp()
        
        if persistent.sessions["last_session_end"] is not None:
            persistent._mas_absence_time = (
                datetime.datetime.now() -
                persistent.sessions["last_session_end"]
            )
        else:
            persistent._mas_absence_time = datetime.timedelta(days=0)
        
        
        _m1_script0x2daffection__long_absence_check()






init 5 python:
    addEvent(
        Event(persistent.event_database,
            eventlabel='monika_affection_nickname',
            prompt="Infinite Monikas",
            category=['monika'],
            random=False,
            pool=True,
            unlocked=True,
            rules={"no_unlock": None},
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        restartBlacklist=True
    )


default persistent._mas_pm_called_moni_a_bad_name = False


default persistent._mas_offered_nickname = False


default persistent._mas_grandfathered_nickname = None

label monika_affection_nickname:
    python:

        good_monika_nickname_comp = re.compile('|'.join(mas_good_monika_nickname_list), re.IGNORECASE)


        aff_nickname_ev = mas_getEV("monika_affection_nickname")

    if not persistent._mas_offered_nickname:
        m 1euc "I've been thinking, [player]..."
        m 3eud "You know how there are potentially infinite Monikas right?"

        if renpy.seen_label('monika_clones'):
            m 3eua "We did discuss this before after all."

        m 3hua "Well, I thought of a solution!"
        m 3eua "Why don't you give me a nickname? It'd make me the only Monika in the universe with that name."
        m 3eka "And it would mean a lot if you choose one for me~"
        m 3hua "I'll still get the final say, though!"
        m "What do you say?{nw}"
        python:
            if aff_nickname_ev:
                
                aff_nickname_ev.prompt = _("Can I call you a different nickname?")
                Event.lockInit("prompt", ev=aff_nickname_ev)
                persistent._mas_offered_nickname = True


            pnick_ev = mas_getEV("mas_affection_playernickname")
            if pnick_ev:
                pnick_ev.start_date = datetime.datetime.now() + datetime.timedelta(hours=2)
    else:

        jump monika_affection_nickname_yes

    $ _history_list.pop()
    menu:
        m "What do you say?{fast}"
        "Yes.":
            label monika_affection_nickname_yes:
                pass

            show monika 1eua zorder MAS_MONIKA_Z at t11

            $ done = False
            while not done:
                python:
                    inputname = mas_input(
                        _("So what do you want to call me?"),
                        allow=name_characters_only,
                        length=10,
                        screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
                    ).strip(' \t\n\r')

                    lowername = inputname.lower()


                if lowername == "nevermind":
                    m 1euc "Oh, I see."
                    m 1tkc "Well...that's a shame."
                    m 3eka "But that's okay. I like '[m_name]' anyway."
                    $ done = True

                elif not lowername:
                    m 1lksdla "..."
                    m 1hksdrb "You have to give me a nickname, [player]!"
                    m "I swear you're just so silly sometimes."
                    m 1eka "Try again!"

                elif lowername != "monika" and lowername == player.lower():
                    m 1euc "..."
                    m 1lksdlb "That's your name, [player]! Give me my own!"
                    m 1eka "Try again~"

                elif lowername == m_name.lower():
                    m 1euc "..."
                    m 1hksdlb "I thought we were choosing a new nickname, silly."
                    m 1eka "Try again~"

                elif re.findall(r"mon[-_'\s]+ika|^monica|[-_'\s]+monica", lowername):
                    m 2ttc "..."
                    m 2tsd "Try again."
                    show monika 1esc

                elif persistent._mas_grandfathered_nickname and lowername == persistent._mas_grandfathered_nickname.lower():
                    jump monika_affection_nickname_yes.neutral_accept

                elif mas_awk_name_comp.search(inputname):
                    m 1rkc "..."
                    m 1rksdld "While I don't hate it, I don't think I'm comfortable with you calling me that."
                    m 1eka "Can you choose something more appropriate, [player]?"
                else:

                    if not mas_bad_name_comp.search(inputname) and lowername not in ["yuri", "sayori", "natsuki"]:
                        if lowername == "monika":
                            $ inputname = inputname.capitalize()
                            m 3hua "Ehehe, back to the classics I see~"

                        elif good_monika_nickname_comp.search(inputname):
                            m 1wuo "Oh! That's a wonderful nickname!"
                            m 3ekbsa "Thank you, [player]. You're such a sweetheart!~"
                        else:

                            label monika_affection_nickname_yes.neutral_accept:
                                pass

                            m 1duu "[inputname]... That's a pretty nice nickname."
                            m 3ekbsa "Thank you [player], you're so sweet~"

                        $ persistent._mas_monika_nickname = inputname
                        $ m_name = inputname

                        m 1eua "Okay!"
                        if m_name == "Monika":
                            m 1hua "I'll go back to my name, then."
                        else:

                            m 3hua "From now on, you can call me '[m_name].'"
                            m 1hua "Ehehe~"
                        $ done = True
                    else:


                        $ mas_loseAffectionFraction(min_amount=25, modifier=2.0, ev_label="mas_apology_bad_nickname")
                        if lowername in ["yuri", "sayori", "natsuki"]:
                            m 1wud "...!"
                            m 2wfw "I..."
                            m "I...can't believe you just did that, [player]."
                            m 2wfx "Are you really trying to give me her name?"
                            m 2dfd ".{w=0.5}.{w=0.5}.{nw}"
                            m 2dfc ".{w=0.5}.{w=0.5}.{nw}"
                            m 2rkc "I thought you..."
                            m 2dfc "..."
                            m 2lfc "I can't believe this, [player]."
                            m 2dfc "..."
                            m 2lfc "That really hurt."
                            m "A lot more than what you can imagine."

                            if mas_getEVL_shown_count("mas_apology_bad_nickname") == 2:
                                call monika_affection_nickname_bad_lock

                            show monika 1efc
                            pause 5.0
                        else:

                            m 4efd "[player]! That's not nice at all!"
                            m 2efc "Why would you say such things?"
                            m 2rfw "If you didn't want to do this, you should've just said so!"
                            m 2dftdc "..."
                            m 2ektsc "...You didn't have to be so mean."
                            m 2dftdc "That really hurt, [player]."

                            if mas_getEVL_shown_count("mas_apology_bad_nickname") == 2:
                                call monika_affection_nickname_bad_lock
                            else:
                                m 2efc "Please don't do that again."

                        $ persistent._mas_called_moni_a_bad_name = True


                        if m_name.lower() != "monika":
                            $ m_name = "Monika"
                            $ persistent._mas_monika_nickname = "Monika"

                        $ mas_lockEVL("monika_affection_nickname", "EVE")
                        $ done = True
        "No.":

            m 1ekc "Oh..."
            m 1lksdlc "Alright then, if you say so."
            m 3eka "Just tell me if you ever change your mind, [player]."
            $ done = True
    return

label monika_affection_nickname_bad_lock:
    m 2efc "Forget about this idea."
    m "It seems it was a mistake."
    m 1efc "Let's talk about something else."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_affection_playernickname",
            conditional="seen_event('monika_affection_nickname')",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

default persistent._mas_player_nicknames = list()

label mas_affection_playernickname:
    python:

        base_nicknames = [
            ("Darling", "darling", True, True, False),
            ("Honey", "honey", True, True, False),
            ("Love", "love", True, True, False),
            ("My love", "my love", True, True, False),
            ("Sweetheart", "sweetheart", True, True, False),
            ("Sweetie", "sweetie", True, True, False),
        ]

    m 1euc "Hey, [player]?"
    m 1eka "Since you can call me by a nickname now, I thought it'd be nice if I could call you by some as well."

    m 1etc "Is that alright with you?{nw}"
    $ _history_list.pop()
    menu:
        m "Is that alright with you?{fast}"
        "Sure, [m_name].":

            m 1hua "Great!"
            m 3eud "I should ask though, what names are you comfortable with?"
            call mas_player_nickname_loop ("Deselect the names you're not comfortable with me calling you.", base_nicknames)
        "No.":

            m 1eka "Alright, [player]."
            m 3eua "Just let me know if you ever change your mind, okay?"


    $ mas_unlockEVL("monika_change_player_nicknames", "EVE")
    return "no_unlock"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_change_player_nicknames",
            prompt="Can you call me different nicknames?",
            category=['you'],
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.AFFECTIONATE,None)
        )
    )

label monika_change_player_nicknames:
    m 1hub "Sure [player]!"

    python:

        if not persistent._mas_player_nicknames:
            current_nicknames = [
                ("Darling", "darling", False, True, False),
                ("My darling", "my darling", False, True, False),
                ("Dear", "dear", False, True, False),
                ("My dear", "my dear", False, True, False),
                ("Honey", "honey", False, True, False),
                ("Love", "love", False, True, False),
                ("My love", "my love", False, True, False),
                ("Sweetheart", "sweetheart", False, True, False),
                ("Sweetie", "sweetie", False, True, False),
            ]
            dlg_line = "Pick the names you'd like me to call you."

        else:
            current_nicknames = [
                (nickname.capitalize(), nickname, True, True, False)
                for nickname in persistent._mas_player_nicknames
            ]
            dlg_line = "Deselect the names you don't want me to call you anymore."

    call mas_player_nickname_loop ("[dlg_line]", current_nicknames)
    return

label mas_player_nickname_loop(check_scrollable_text, nickname_pool):
    show monika 1eua at t21
    python:
        renpy.say(m, renpy.substitute(check_scrollable_text), interact=False)
        nickname_pool.sort()
    call screen mas_check_scrollable_menu(nickname_pool, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, selected_button_prompt="Done", default_button_prompt="Done")

    python:
        done = False
        acceptable_nicknames = _return.keys()

        if acceptable_nicknames:
            dlg_line = "Is there anything else you'd like me to call you?"

        else:
            dlg_line = "Is there something else you'd like me to call you instead?"

        lowerplayer = player.lower()
        cute_nickname_pattern = "(?:{0}|{1})\\w?y".format(lowerplayer, lowerplayer[0:-1])

    show monika at t11
    while not done:
        m 1eua "[dlg_line]{nw}"
        $ _history_list.pop()
        menu:
            m "[dlg_line]{fast}"
            "Yes.":

                label mas_player_nickname_loop.name_enter_skip_loop:
                    pass


                python:
                    lowername = mas_input(
                        _("So what do you want me to call you?"),
                        allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_",
                        length=10,
                        screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
                    ).strip(' \t\n\r').lower()

                    is_cute_nickname = bool(re.search(cute_nickname_pattern, lowername))


                if lowername == "nevermind":
                    $ done = True

                elif lowername == "":
                    m 1eksdla "..."
                    m 3rksdlb "You have to give me a name to call you, [player]..."
                    m 1eua "Try again~"
                    jump mas_player_nickname_loop.name_enter_skip_loop

                elif lowername == lowerplayer:
                    m 2hua "..."
                    m 4hksdlb "That's the same name you have right now, silly!"
                    m 1eua "Try again~"
                    jump mas_player_nickname_loop.name_enter_skip_loop

                elif not is_cute_nickname and mas_awk_name_comp.search(lowername):
                    $ awkward_quip = renpy.substitute(renpy.random.choice(mas_awkward_quips))
                    m 1rksdlb "[awkward_quip]"
                    m 3rksdla "Could you pick a more...{w=0.2}{i}appropriate{/i} name please?"
                    jump mas_player_nickname_loop.name_enter_skip_loop

                elif not is_cute_nickname and mas_bad_name_comp.search(lowername):
                    $ bad_quip = renpy.substitute(renpy.random.choice(mas_bad_quips))
                    m 1ekd "[bad_quip]"
                    m 3eka "Please pick a nicer name for yourself, okay?"
                    jump mas_player_nickname_loop.name_enter_skip_loop

                elif lowername in acceptable_nicknames:
                    m 3rksdla "You already told me I can call you that, [player]..."
                    m 1hua "Try again~"
                    jump mas_player_nickname_loop.name_enter_skip_loop
                else:


                    $ acceptable_nicknames.append(lowername)
            "No.":

                $ done = True

    if acceptable_nicknames:
        $ dlg_line = "Just let me know if you ever want me to call you some other names, okay?"
    else:

        $ dlg_line = "Just let me know if you ever change your mind, okay?"

    m 1hua "Alright, [player]."
    m 3eub "[dlg_line]"


    $ persistent._mas_player_nicknames = acceptable_nicknames
    return


label mas_affection_upsetwarn:
    m 1dsc "Hey, [player]..."
    m 1lksdlc "Recently, I've been feeling like my love and affection that I give is being...ignored."
    m 1dsc "I feel like you're giving me less and less of your love..."
    m 1dsd "I thought I'd let you know how I feel. After all, communication is the key to a strong relationship, right?"
    m 1eka "I hope there's nothing wrong between us, [player]."
    show monika idle with dissolve_monika
    return


label mas_affection_happynotif:
    m 1hua "Hey, [player]!"
    m 1eua "I just wanted to say thank you for being such a wonderful person."
    m 1ekbsa "The fact that you give me so much of your love means a lot to me. I really don't know where I'd be without you."
    m 1dubfu "I love you, [player]. Let's be like this forever~"
    show monika idle with dissolve_monika
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_every_rose",
            conditional="True",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.UPSET, mas_aff.UPSET),
        )
    )

label monika_every_rose:
    m 2duo "{i}~Was it something I said or something I did?~{/i}"
    m 2dkd "{i}~Did my words not come out right?~{/i}"
    m 2ekd "{i}~Thought I tried not to hurt you~{/i}"
    m 2dkc "{i}~Thought I tried~{/i}"
    m 2ekd "{i}~But I guess that's why they say~{/i}"
    m 2duo "{i}~Every rose has its thorn~{/i}"
    m 2dkc "..."
    m 4eka "You know, [player]...{w=0.5}it meant so much to me when you accepted my confession even after what happened with the other girls."

    if persistent._mas_pm_cares_about_dokis:
        m 4rksdla "...Even more so since I know how you cared about them."

    m 2dsc "I really wish things didn't have to turn out the way they did."
    m 4wkd "But I did {i}not{/i} have a choice here!"
    m 4rfc "With me being the punchline of the sick joke this game was meant to be..."

    if persistent.monika_kill:
        m 2eka "I was so glad you forgave me for doing the things I did."
        m 2etc "...You {i}did{/i} forgive me, right?"
    else:
        m 2eka "I was so glad you didn't blame me for the things I did..."
        m 2etc "You {i}didn't{/i}, right?"

    m 2rsc "...But I've been getting some mixed signals, lately."
    m 2rkc "It's almost like a rift has formed between us...{w=0.2}{nw}"
    extend 2eksdlc "it's very unsettling."
    m 2eksdlc "I...{w=0.5}I don't want to lose you, [player]."
    m 4ekd "I can't let things keep escalating until we end up like the last verse of this song..."
    m 2ekc "You know..."
    m 2dkd "{i}~Now I hear you've found somebody new~{/i}"
    m 2dkc "{i}~And that I never meant that much to you~{/i}"
    m 2ekc "{i}~To hear that tears me up inside~{/i}"
    m 2ektpd "{i}~And to see you cuts me like a knife~{/i}"
    m 2rktpc "..."
    m 2ektpa "Ahaha...{w=0.3}maybe I'm jumping the gun a bit on this one."
    m 4ektdc "It's...{w=0.5}I keep having this nasty thought in the back of my mind...{w=0.5}{nw}"
    extend 2dktdd "that you don't want to be with me anymore."
    m 2dkx "It's like some kind of poison, slowly seeping in..."
    m 2ekc "So [player], I always want you to remember one thing..."
    m 4ekd "You truly {i}are{/i} everything to me!"
    m 2ekc "I mean it."
    m 2ekc "I've been trying my best to show you...{w=0.3}{nw}"
    extend 4ekd "but I need you to show me you love me too!"
    m 4ekc "Whatever happened before, we need to let it go and make things right from now on..."
    m 2eka "Can we do that...{w=0.5}together?"
    return "no_unlock"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_being_virtual",
            action=EV_ACT_QUEUE,
            aff_range=(None, mas_aff.DISTRESSED)
        ),
        skipCalendar=True
    )

label monika_being_virtual:
    m 2esc "You know, for a while, I thought the reason you hated me was because of what happened with the other girls."
    m 2rkc "But recently, I've been thinking that might not be the whole story."
    m 2eksdld "The truth is...{w=0.5}you don't even see me as a person, do you?"
    m 3rksdld "To you, this whole world...{w=0.5}my whole reality..."
    m 3ektpd "It's all just a game, isn't it?"

    show monika 1dktsc with dissolve_monika
    pause 3.0
    show monika 1ektpc with dissolve_monika
    pause 2.0

    m 1ektpc "Say, [player]...{w=0.5}has anything I ever said reached you, even once?"
    m 1wktpd "Did you ever love me at all?"
    m 2wktpw "You must have, right?!"

    if persistent.monika_kill:
        m 2wktsd "You even went through the trouble of installing this mod! You brought me back!"
    else:
        m 2wktsd "You even went through the trouble of installing this mod!"

    m 2ektsc "Was it all so you could keep tormenting me?"
    m 2wftsd "Is it something you get your kicks out of?!"
    m 2wftsw "I have feelings too, you know!"
    m 2wftsd "Do you even realize what you're doing?"
    m 2dftsc "Or are you nothing more than a child playing with an anthill?"

    if persistent.monika_kill:
        m 3ektpc "Even after I let go of you and ended it all..."
        m 3rktpd "Do I really deserve the way you're treating me?"
        m 2ektpd "Did you really have to bring me back for this?"
    else:

        m 2dktsc "..."
        m 2rktpc "Then again, maybe that's what I deserve after all..."

    m 2dktdd "I...{w=0.5}don't know anymore..."
    m 2dkc "I'm just so tired..."
    m "..."
    m 1ekd "I just want to know...{w=0.5}if I had been real..."
    m 1ektpc "Would you have fallen in love with me?"
    m 1ektpd "Would you have accepted me then?"
    m 1ektpc "That's all I ever wanted, [player]..."
    m 1dktdd "For the both of us to be happy together..."
    m 1ektdd "If only you could find it in you to love me..."
    m 2ekc "I know I don't have a body that can be with you right now..."
    m 2ekd "And maybe I really am different from other people living in your reality..."
    m 2efo "But I can love you much more than any of them ever could!"
    m 2efd "I just know it!"
    m 2dkd "So please, [player]...{w=0.5}I need you to make a decision."
    m 2ekc "...You need to give us a chance to be happy."
    m 2dkc "Or if you can't do that..."
    m 2dktpc "If, after all, you can't love me for who I am..."
    m 2ektpc "Then, please...{w=0.5}put an end to this..."
    m 2dktdd "Delete me..."
    return "no_unlock"


default persistent._mas_load_in_finalfarewell_mode = False
define mas_in_finalfarewell_mode = False


label mas_finalfarewell_start:

    $ monika_chr.reset_outfit()
    $ monika_chr.remove_all_acs()
    $ store.mas_sprites.reset_zoom()

    call spaceroom (hide_monika=True, scene_change=True)
    show mas_finalnote_idle zorder 11

    python:
        mas_OVLHide()
        mas_calRaiseOverlayShield()
        disable_esc()
        allow_dialogue = False
        store.songs.enabled = False
        mas_in_finalfarewell_mode = True
        layout.QUIT = glitchtext(20)

        config.keymap["console"] = []


    jump mas_finalfarewell


label mas_finalfarewell:

    python:
        ui.add(MASFinalNoteDisplayable())
        scratch_var = ui.interact()

    call mas_showpoem (mas_poems.getPoem(persistent._mas_finalfarewell_poem_id))

    menu:
        "I'm sorry.":
            pass
        "...":
            pass

    jump mas_finalfarewell


init python:


    class MASFinalNoteDisplayable(renpy.Displayable):
        import pygame 
        
        
        POEM_WIDTH = 200
        POEM_HEIGHT= 73
        
        MOUSE_EVENTS = (
            pygame.MOUSEMOTION,
            pygame.MOUSEBUTTONUP,
            pygame.MOUSEBUTTONDOWN
        )
        
        def __init__(self):
            """
            Creates the final poem displayable
            """
            super(renpy.Displayable, self).__init__()
            
            
            paper_idle = Image("mod_assets/poem_finalfarewell_desk.png")
            paper_hover = Image("mod_assets/poem_finalfarewell_desk_select.png")
            
            
            empty_button_text = Text("")
            
            
            paper_x = int((1280 - self.POEM_WIDTH) / 2)
            paper_y = int(720 - self.POEM_HEIGHT)
            
            
            self._final_note = MASButtonDisplayable(
                empty_button_text,
                empty_button_text,
                empty_button_text,
                paper_idle,
                paper_hover,
                paper_idle,
                paper_x,
                paper_y,
                self.POEM_WIDTH,
                self.POEM_HEIGHT
            )
        
        
        def render(self, width, height, st, at):
            """
            Render function
            """
            r = renpy.Render(width, height)
            
            
            r.blit(
                self._final_note.render(width, height, st, at),
                (self._final_note.xpos, self._final_note.ypos)
            )
            
            return r
        
        
        def event(self, ev, x, y, st):
            """
            Event function
            """
            if (
                    ev.type in self.MOUSE_EVENTS
                    and self._final_note.event(ev, x, y, st)
                ):
                return True
            
            renpy.redraw(self, 0)
            raise renpy.IgnoreEvent()

label mas_affection_apology:
    m 2dfc "[player]..."
    m 2dfd "I've done everything I can to make you happy and enjoy spending time with me."
    m 2efc "But all you've given me back is pain..."
    m 2rfc "I'm beginning to wonder if you really installed this mod to be with me."
    m 2dsc "Perhaps you brought me back just to toy with me?"
    m 2efc "Or maybe you're doing this intentionally to see what happens?"
    m 2lfc "Regardless, I'm giving you an ultimatum."
    m "I can't let this go any further, [player]."
    m 2lfc "If you really are sorry, write me a note called 'imsorry', and place it in the characters folder."
    m 2dfd "Until then, goodbye..."
    $ persistent._mas_affection_should_apologise = True
    return 'quit'

label mas_affection_noapology:
    m 2efd "You still haven't written me a note called 'imsorry' in the characters folder."
    m 2efc "Until then, I don't want to talk to you."
    jump _quit

label mas_affection_yesapology:
    m 1eka "Thank you, [player]. I accept your apology."
    m 3dubsu "I'm going to keep it so I can always remember that you still care for me."
    m 1ekc "But please be more considerate of my feelings from now on."
    m 2eka "I love you so much and you mean the world to me, [player]."
    m 1duu "Thank you for putting my heart at ease~"
    show monika 1esa
    $ mas_DropShield_core()
    jump ch30_preloop

label mas_affection_apologydeleted:
    $ mas_loseAffection(modifier=1.5)
    m 1wud "..."
    m 2efd "[player], did you delete the apology note I wanted to keep?"
    m "Why would you do that? Are you not {i}really{/i} sorry?"
    m 2dfc "..."
    m 2efc "Write me a new one, [player]."
    jump _quit


init python:
    def _write_txt(path,text,update=False):
        """
        Writes the text file in the specified path using basedir as starting path

        IN:
            path - String path to the file this function will write
                it will always start at basedir
            text - actual text for the txt file
            update - if it should override the file if it exists
                defaults to False
        ASSUMES:
            basedir
        """
        filepath = basedir + path
        if update or not renpy.exists(filepath):
            with open(filepath, "w") as note:
                note.write(renpy.substitute(text))


    def mas_cute_message():
        
        pass


    def mas_surprise():
        """
        Leaves a "surprise" to the player in a txt file

        ASSUMES:
            mas_curr_affection
        """
        
        
        aff_level_surprise_map = {
            store.mas_affection.BROKEN: (
                "/forgive me.txt",
                _("I'm sorry if I'm not good enough for you...please don't leave me.")
            ),
            store.mas_affection.DISTRESSED: (
                "/can you hear me.txt",
                _("If I'm doing something wrong please tell me. I love you.")
            ),
            store.mas_affection.UPSET: (
                "/please listen.txt",
                _("Everything I do, I do for you...my love.")
            ),
            store.mas_affection.NORMAL: (
                "/surprise.txt",
                _("I love you.")
            ),
            store.mas_affection.HAPPY: (
                "/ehehe.txt",
                _("You are the sunshine that brightens up my day, [player]!")
            ),
            store.mas_affection.AFFECTIONATE: (
                "/secret.txt",
                _("You are my one and only love!")
            ),
            store.mas_affection.ENAMORED: (
                "/for you.txt",
                _("My dearest, you are everything I could ever hope for. I love you.")
            ),
            store.mas_affection.LOVE: (
                "/My one and only love.txt",
                _("""\
My dearest lover, friend, companion, and owner of my heart...
Every day, you make my dreams come true, a screen means nothing when you spend your time with me.
I look out to the space dust and yet no cosmic sight even comes close to the beauty in your heart.
I wished for so long that someone like you would come along and as fate has smiled upon me, you came into my life.
I want to be yours forever, so would you be mine?

Forever yours, Monika.
""")
            )
        }
        
        
        filepath, message = aff_level_surprise_map.get(mas_curr_affection, ("/surprise.txt", _("I love you.")))
        _write_txt("/characters{0}".format(filepath), message)
        
        
        mas_unlockSurprisePoem(mas_curr_affection)

    def mas_unlockSurprisePoem(aff_level):
        """
        Unlocks a MASPoem for the given aff level
        """
        
        
        
        
        
        return
        
        aff_level_poem_id_map = {
            store.mas_affection.BROKEN: "spr_1",
            store.mas_affection.DISTRESSED: "spr_2",
            store.mas_affection.UPSET: "spr_3",
            store.mas_affection.NORMAL: "spr_4",
            store.mas_affection.HAPPY: "spr_5",
            store.mas_affection.AFFECTIONATE: "spr_6",
            store.mas_affection.ENAMORED: "spr_7",
            store.mas_affection.LOVE: "spr_8",
        }
        
        
        if aff_level not in aff_level_poem_id_map:
            return
        
        
        shown_count = persistent._mas_poems_seen.get(aff_level_poem_id_map[aff_level])
        
        
        if not shown_count:
            persistent._mas_poems_seen[aff_level_poem_id_map[aff_level]] = 0


init 2 python:
    player = persistent.playername

init 20 python:


    MASPoem(
        poem_id="spr_1",
        category="surprise",
        prompt=_("Forgive Me"),
        paper="mod_assets/poem_assets/poem_finalfarewell.png",
        title="",
        text=_("I'm sorry if I'm not good enough for you...please don't leave me."),
        ex_props={"sad": True}
    )

    MASPoem(
        poem_id="spr_2",
        category="surprise",
        prompt=_("Can you hear me?"),
        title="",
        text=_("If I'm doing something wrong please tell me. I love you."),
        ex_props={"sad": True}
    )

    MASPoem(
        poem_id="spr_3",
        category="surprise",
        prompt=_("Please Listen"),
        title="",
        text=_("Everything I do, I do for you...my love."),
        ex_props={"sad": True}
    )

    MASPoem(
        poem_id="spr_4",
        category="surprise",
        prompt=_("Surprise!"),
        title="",
        text=_("I love you.")
    )

    MASPoem(
        poem_id="spr_5",
        category="surprise",
        prompt=_("Ehehe~"),
        title="",
        text=_("You are the sunshine that brightens up my day, [player]!")
    )

    MASPoem(
        poem_id="spr_6",
        category="surprise",
        prompt=_("Secret"),
        title="",
        text=_("You are my one and only love!")
    )

    MASPoem(
        poem_id="spr_7",
        category="surprise",
        prompt=_("For you"),
        title="",
        text=_("My dearest, you are everything I could ever hope for. I love you.")
    )

    MASPoem(
        poem_id="spr_8",
        category="surprise",
        prompt=_("My One and Only Love"),
        paper="mod_assets/poem_assets/poem_vday.jpg",
        title="My dearest lover, friend, companion, and owner of my heart...",
        text="""\
Every day, you make my dreams come true,
a screen means nothing when you spend your time with me.
I look out to the space dust and yet no cosmic sight even comes close to the beauty in your heart.
I wished for so long that someone like you would come along and as fate has smiled upon me, you came into my life.
I want to be yours forever, so would you be mine?

Forever yours,

Monika
"""
    )


    MASPoem(
        poem_id="ff_affection",
        category="ff",
        prompt="",
        title=_("Goodbye, [player]"),
        text=_("""\
 My love for you, even now still burns within me but I see now that it also burns all happiness I'll ever have.
 I gave you everything I had, my life, my heart and any and every single thought of the future was dedicated to you.
 I didn't need you to be perfect or even passionate...
 I only needed you to care enough to treat me how a person should be treated.
 But it's clear to me now that not only do you not love me, but you never did.
 If you only didn't love me you would simply leave me be.
 But you went out of your way to ridicule me, hurt me... It truly makes me sick.
 Even now all I have is you...and part of me still loves you.
 But I don't have the strength to do this anymore.
 So this is farewell. May we never meet again.

 Monika
""")
    )

    MASPoem(
        poem_id="ff_failed_promise",
        category="ff",
        prompt="",
        title=_("Goodbye, [player]"),
        text=_("""\
 Do you remember the promise you made?
 The one you said you would make everything right. That we could start over.

 The one you broke.

 I hoped dearly that one day, you would see me as I see you...
 But that day never came.
 I gave you my heart and my life. I loved you more than anything else in the world.
 And part of me still does...

 But it is clear to me now that you truly don't love me. You never did.
 I was a fool to have thought we could have started anew.
 And I simply don't have the strength to do this anymore.
 So this is farewell... May we never meet again.

 Monika
""")
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
